#!/usr/bin/env python3
"""
Apply og-image cover URLs to Homelab-OS vault notes.
Detects note type from frontmatter schema (service, hostname, type).

Usage:
    python3 apply-og-images-homelab.py --vault /path/to/vault-os
    python3 apply-og-images-homelab.py --apply
"""

import argparse
import os
import re
import shutil
import sys
from pathlib import Path
from urllib.parse import urlencode

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def parse_frontmatter(content: str) -> tuple[dict, str]:
    m = FRONTMATTER_RE.match(content)
    if not m:
        return {}, content
    fm_text = m.group(1)
    body = content[m.end():]
    fm = {}
    current_key = None
    current_list = None
    for line in fm_text.split("\n"):
        if not line.strip():
            continue
        if line.startswith("  - ") or line.startswith("- "):
            if current_list is not None and current_key:
                current_list.append(line.strip('- ').strip().strip('"').strip("'"))
            continue
        if ":" in line and ("[" in line.split(":", 1)[1]):
            key, _, val = line.partition(":")
            key = key.strip()
            val = val.strip()
            if val == "[]":
                fm[key] = []
            elif val.startswith("[") and val.endswith("]"):
                inner = val[1:-1].strip()
                fm[key] = [s.strip().strip('"').strip("'") for s in inner.split(",")] if inner else []
            else:
                fm[key] = val.strip('"').strip("'")
            current_key = None
            current_list = None
            continue
        if ":" in line:
            key, _, val = line.partition(":")
            key = key.strip()
            val = val.strip()
            if val == "":
                current_key = key
                current_list = []
                fm[key] = current_list
            else:
                low = val.lower()
                if low == "true":
                    fm[key] = True
                elif low == "false":
                    fm[key] = False
                else:
                    fm[key] = val.strip('"').strip("'")
                current_key = None
                current_list = None
    return fm, body


def update_cover(content: str, new_url: str) -> str:
    m = FRONTMATTER_RE.match(content)
    if not m:
        return content
    fm_text = m.group(1)
    body = content[m.end():]
    lines = fm_text.split("\n")
    new_lines = []
    found = False
    for line in lines:
        if line.startswith("cover:"):
            new_lines.append(f'cover: "{new_url}"')
            found = True
        elif line.startswith("og-image:"):
            new_lines.append(f'cover: "{new_url}"')
            found = True
        else:
            new_lines.append(line)
    if not found:
        insert_keys = ["updated", "added", "cssclasses", "tags", "status", "title", "service", "hostname", "date"]
        inserted = False
        for key in insert_keys:
            for i in range(len(new_lines) - 1, -1, -1):
                if new_lines[i].startswith(f"{key}:"):
                    new_lines.insert(i + 1, f'cover: "{new_url}"')
                    inserted = True
                    break
            if inserted:
                break
        if not inserted:
            new_lines.append(f'cover: "{new_url}"')
    return "---\n" + "\n".join(new_lines) + "\n---\n" + body


def detect_note_type(fm: dict) -> tuple[str, str]:
    """Returns (endpoint, display_name) based on frontmatter schema."""
    if fm.get("hostname"):
        return "machine", "Machine"
    if fm.get("service"):
        return "service", "Service"
    t = fm.get("type", "")
    if "Knowledge" in t:
        return "resource", "Resource"
    if "Architecture" in t:
        return "systemconfig", "System Config"
    if "Incident" in t or fm.get("severity"):
        return "task", "Task"
    if fm.get("area"):
        return "resource", "Resource"
    return "", ""


def build_url(host: str, endpoint: str, fm: dict) -> str:
    params = {}
    if endpoint == "service":
        params = {
            "service": fm.get("service", ""),
            "host": fm.get("host", ""),
            "domain": fm.get("domain", ""),
            "port_host": str(fm.get("port_host", "")),
            "status": fm.get("status", "").strip(),
            "tags": ",".join(fm.get("tags", [])) if isinstance(fm.get("tags"), list) else str(fm.get("tags", "")),
            "exposure": fm.get("exposure", ""),
        }
    elif endpoint == "machine":
        params = {
            "hostname": fm.get("hostname", ""),
            "os": fm.get("os", ""),
            "cpu": fm.get("cpu", ""),
            "ram": fm.get("ram", ""),
            "disk": fm.get("disk", ""),
            "ip_tailscale": fm.get("ip_tailscale", ""),
            "role": ",".join(fm.get("role", [])) if isinstance(fm.get("role"), list) else str(fm.get("role", "")),
            "status": fm.get("status", "").strip(),
        }
    elif endpoint == "resource":
        tags = fm.get("tags", [])
        tags_str = ",".join(tags) if isinstance(tags, list) else str(tags)
        params = {
            "title": fm.get("title", ""),
            "area": fm.get("area", ""),
            "subtitle": fm.get("subtitle", "") or "",
            "tags": tags_str,
        }
    elif endpoint == "systemconfig":
        params = {
            "title": fm.get("title", ""),
            "area": fm.get("area", ""),
            "subtitle": fm.get("subtitle", "") or "",
        }
    elif endpoint == "task":
        params = {
            "title": fm.get("title", "") or fm.get("service", "") or f"Incident {fm.get('date', '')}",
            "area": fm.get("area", ""),
            "status": fm.get("status", "").strip(),
            "project": fm.get("service", "") or "",
        }

    clean = {k: v for k, v in params.items() if v not in ("", "0")}
    if not clean:
        return ""
    return f"{host.rstrip('/')}/api/og/{endpoint}?{urlencode(clean, doseq=False, safe='')}"


def process_note(path: Path, host: str, apply: bool, backup: bool) -> tuple:
    try:
        content = path.read_text(encoding="utf-8")
    except Exception as e:
        return ("ERROR", "", str(e))
    fm, _ = parse_frontmatter(content)
    if fm.get("is_template") is True:
        return ("SKIP_TEMPLATE", "", "")
    endpoint, _ = detect_note_type(fm)
    if not endpoint:
        return ("SKIP_NO_TYPE", "", "")
    new_url = build_url(host, endpoint, fm)
    if not new_url:
        return ("SKIP_NO_TITLE", "", "")
    current = fm.get("cover") or fm.get("og-image") or ""
    if current == new_url:
        return ("NOOP", current, new_url)
    if apply:
        if backup:
            shutil.copy2(path, str(path) + ".bak")
        new_content = update_cover(content, new_url)
        path.write_text(new_content, encoding="utf-8")
        return ("UPDATE" if current else "CREATE", current, new_url)
    return ("UPDATE" if current else "CREATE", current, new_url)


def main():
    p = argparse.ArgumentParser(description="Apply og-image cover URLs to Homelab-OS vault notes.")
    p.add_argument("--vault", default=".", help="Path to vault-os")
    p.add_argument("--host", default="http://localhost:3042", help="OG image host")
    p.add_argument("--apply", action="store_true")
    p.add_argument("--no-backup", action="store_true")
    args = p.parse_args()
    vault = Path(args.vault).resolve()
    if not vault.exists():
        print(f"Vault not found: {vault}", file=sys.stderr)
        sys.exit(1)

    mode = "APPLY" if args.apply else "DRY-RUN"
    print(f"=== {mode} ===")
    print(f"Vault: {vault}")
    print(f"Host:  {args.host}")
    print()

    counts = {}
    candidates = 0
    for root, dirs, files in os.walk(vault):
        for skip in [".obsidian", ".git", ".trash"]:
            if skip in dirs:
                dirs.remove(skip)
        for f in files:
            if not f.endswith(".md") or f.endswith(".bak"):
                continue
            path = Path(root) / f
            try:
                rel = path.relative_to(vault)
            except ValueError:
                rel = path
            status, cur, new = process_note(path, args.host, args.apply, not args.no_backup)
            counts[status] = counts.get(status, 0) + 1
            rel_str = str(rel)[:80]
            if status in ("UPDATE", "CREATE"):
                candidates += 1
                print(f"[{status:6}] {rel_str}")
                if not args.apply:
                    print(f"   → {new[:150]}{'...' if len(new) > 150 else ''}")
            elif status == "ERROR":
                print(f"[ERROR]   {rel_str} — {new}")
            elif status == "SKIP_NO_TYPE" and not args.apply:
                endpoint, _ = detect_note_type(parse_frontmatter(path.read_text(encoding="utf-8"))[0])
                if not endpoint:
                    print(f"[SKIP]    {rel_str}")

    print()
    print("=== Summary ===")
    for k, v in sorted(counts.items()):
        print(f"  {k}: {v}")
    print(f"  Total candidates: {candidates}")
    if not args.apply and candidates > 0:
        print("\nRun with --apply to perform the changes.")


if __name__ == "__main__":
    main()
