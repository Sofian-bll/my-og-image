#!/usr/bin/env python3
"""
Apply og-image URLs to all notes in an Obsidian vault.

Usage:
    python3 apply-og-images.py                    # dry-run
    python3 apply-og-images.py --apply            # apply changes
    python3 apply-og-images.py --host https://og.sofian.lab
    python3 apply-og-images.py --vault /path/to/vault
    python3 apply-og-images.py --no-backup
"""

import argparse
import os
import re
import shutil
import sys
from pathlib import Path
from urllib.parse import quote, urlencode


# ---------- Type → endpoint mapping ----------

TYPE_MAPPING = {
    "📂 Project": "project",
    "📚 Resource": "resource",
    "📄 Resource": "resource",
    "✏️ Task": "task",
    "🌱 Aspiration": "aspiration",
    "⚙️ System Config": "systemconfig",
}

# Endpoints that take the Epitech-specific URL pattern
EPITECH_TYPES = {"epitechproject"}


# ---------- Helpers ----------

def clean_area(area: str) -> str:
    """Strip wiki-link brackets and emojis (Templater behavior)."""
    if not area:
        return ""
    return re.sub(r"[\[\]]", "", area).strip()


def strip_wikilink(value: str) -> str:
    """Remove [[ ]] and emojis from a value (for project names etc.)."""
    if not value:
        return ""
    cleaned = re.sub(r"[[\]]", "", value)
    cleaned = re.sub(r"[^\w\s]", "", cleaned)
    return cleaned.strip()


def get_status_param(status: str) -> str:
    """Normalize status (lowercase, snake_case)."""
    if not status:
        return ""
    return status.strip().lower().replace(" ", "_")


def build_og_url(host: str, endpoint: str, params: dict) -> str:
    """Build a clean og-image URL. urlencode handles encoding."""
    # Filter out empty values
    clean_params = {k: v for k, v in params.items() if v}
    if not clean_params:
        return ""
    query = urlencode(clean_params, doseq=False, safe="")
    return f"{host.rstrip('/')}/api/og/{endpoint}?{query}"


# ---------- URL builders per type ----------

def url_for_project(host: str, fm: dict) -> str:
    """Standard project (Perso or generic)."""
    title = fm.get("title", "")
    area = clean_area(fm.get("area", ""))
    status = get_status_param(fm.get("status", ""))
    priority = fm.get("priority", "").strip().lower()
    scheduled = fm.get("scheduled_date", "") or ""
    due = fm.get("due_date", "") or ""

    return build_og_url(host, "project", {
        "title": title,
        "area": area,
        "status": status,
        "priority": priority,
        "scheduled_date": scheduled,
        "due_date": due,
    })


def url_for_epitech_project(host: str, fm: dict) -> str:
    """Epitech project uses the dedicated template."""
    title = fm.get("title", "")
    area = clean_area(fm.get("area", ""))
    status = get_status_param(fm.get("status", ""))
    unit_code = fm.get("epitech_unit_code", "")
    kind = fm.get("epitech_kind", "").strip().lower()
    cursus = fm.get("epitech_school_year", "")
    scheduled = fm.get("scheduled_date", "") or ""
    due = fm.get("due_date", "") or ""

    return build_og_url(host, "epitechproject", {
        "title": title,
        "area": area,
        "status": status,
        "epitech_unit_code": unit_code,
        "epitech_kind": kind,
        "epitech_cursus": cursus,
        "scheduled_date": scheduled,
        "due_date": due,
    })


def url_for_resource(host: str, fm: dict) -> str:
    title = fm.get("title", "")
    area = clean_area(fm.get("area", ""))
    tags = fm.get("tags", [])
    if isinstance(tags, list):
        tags_str = ",".join(str(t).strip() for t in tags if t)
    else:
        tags_str = str(tags).strip()

    return build_og_url(host, "resource", {
        "title": title,
        "area": area,
        "tags": tags_str,
    })


def url_for_task(host: str, fm: dict) -> str:
    title = fm.get("title", "")
    area = clean_area(fm.get("area", ""))
    status = get_status_param(fm.get("status", ""))

    # Contexts
    contexts = fm.get("contexts", [])
    if isinstance(contexts, list):
        contexts_str = ",".join(str(c).strip() for c in contexts if c)
    else:
        contexts_str = str(contexts).strip()

    # Project (first entry of projects array, stripped)
    projects = fm.get("projects", [])
    if isinstance(projects, list) and projects:
        project = strip_wikilink(str(projects[0]))
    elif isinstance(projects, str):
        project = strip_wikilink(projects)
    else:
        project = ""

    due = fm.get("due_date", "") or ""

    return build_og_url(host, "task", {
        "title": title,
        "area": area,
        "status": status,
        "contexts": contexts_str,
        "project": project,
        "due_date": due,
    })


def url_for_aspiration(host: str, fm: dict) -> str:
    title = fm.get("title", "")
    description = fm.get("description", "") or ""
    area = clean_area(fm.get("area", ""))

    return build_og_url(host, "aspiration", {
        "title": title,
        "description": description,
        "area": area,
    })


def url_for_systemconfig(host: str, fm: dict) -> str:
    title = fm.get("title", "")
    area = clean_area(fm.get("area", ""))
    subtitle = fm.get("subtitle", "") or ""

    return build_og_url(host, "systemconfig", {
        "title": title,
        "area": area,
        "subtitle": subtitle,
    })


URL_BUILDERS = {
    "project": url_for_project,
    "epitechproject": url_for_epitech_project,
    "resource": url_for_resource,
    "task": url_for_task,
    "aspiration": url_for_aspiration,
    "systemconfig": url_for_systemconfig,
}


# ---------- YAML frontmatter parser (simple) ----------

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def parse_frontmatter(content: str) -> tuple[dict, str]:
    """Returns (frontmatter_dict, body_content). Simple key: value parser."""
    m = FRONTMATTER_RE.match(content)
    if not m:
        return {}, content

    fm_text = m.group(1)
    body = content[m.end():]

    fm = {}
    current_key = None
    current_list = None

    for line in fm_text.split("\n"):
        # Skip empty lines
        if not line.strip():
            continue

        # List item
        if line.startswith("  - "):
            if current_list is not None and current_key:
                current_list.append(line[4:].strip().strip('"').strip("'"))
            continue

        # Inline list: tags: [a, b, c]
        if ":" in line and (line.strip().endswith("[") or "[" in line.split(":", 1)[1]):
            key, _, val = line.partition(":")
            key = key.strip()
            val = val.strip()
            if val == "[]":
                fm[key] = []
            elif val.startswith("[") and val.endswith("]"):
                inner = val[1:-1].strip()
                if inner:
                    fm[key] = [s.strip().strip('"').strip("'") for s in inner.split(",")]
                else:
                    fm[key] = []
            else:
                fm[key] = val.strip('"').strip("'")
            current_key = None
            current_list = None
            continue

        # Key: value or Key: (start of multi-line list)
        if ":" in line:
            key, _, val = line.partition(":")
            key = key.strip()
            val = val.strip()

            if val == "":
                # Could be a multi-line list (next lines start with "  - ")
                current_key = key
                current_list = []
                fm[key] = current_list
            else:
                # Coerce booleans
                if val.lower() == "true":
                    fm[key] = True
                elif val.lower() == "false":
                    fm[key] = False
                else:
                    fm[key] = val.strip('"').strip("'")
                current_key = None
                current_list = None
            continue

    return fm, body


def update_frontmatter_og_image(content: str, new_url: str) -> str:
    """Replace the og-image line in the frontmatter. Adds it if missing."""
    m = FRONTMATTER_RE.match(content)
    if not m:
        return content

    fm_text = m.group(1)
    body = content[m.end():]
    lines = fm_text.split("\n")

    # Try to find existing cover line
    new_lines = []
    found = False
    for line in lines:
        if line.startswith("cover:"):
            new_lines.append(f"cover: \"{new_url}\"")
            found = True
        else:
            new_lines.append(line)

    if not found:
        # Insert after due_date, scheduled_date, or status — in that order
        insert_keys = ["due_date", "scheduled_date", "status", "priority", "area", "title", "type"]

        # Find the rightmost matching key
        for key in insert_keys:
            for i in range(len(new_lines) - 1, -1, -1):
                if new_lines[i].startswith(f"{key}:"):
                    new_lines.insert(i + 1, f"cover: \"{new_url}\"")
                    inserted = True
                    break
            if inserted:
                break

        if not inserted:
            # Fallback: append at end of frontmatter
            new_lines.append(f"cover: \"{new_url}\"")

    new_fm = "\n".join(new_lines)
    return f"---\n{new_fm}\n---\n{body}"


# ---------- Main ----------

def get_endpoint_for_type(type_val: str, area: str) -> str:
    """Returns the endpoint name (e.g., 'epitechproject', 'project') for a given type."""
    base = TYPE_MAPPING.get(type_val)
    if not base:
        return ""
    if base == "project" and "Epitech" in area:
        return "epitechproject"
    return base


def is_epitech(area: str) -> bool:
    return "Epitech" in area


def process_note(path: Path, host: str, apply: bool, backup: bool) -> tuple[str, str, str]:
    """
    Returns (status, current_value, new_value).
    status: 'UPDATE', 'CREATE', 'SKIP_TEMPLATE', 'SKIP_NO_TYPE', 'SKIP_NO_TITLE', 'SKIP_UNKNOWN_TYPE', 'ERROR'
    """
    try:
        content = path.read_text(encoding="utf-8")
    except Exception as e:
        return ("ERROR", "", f"read error: {e}")

    fm, body = parse_frontmatter(content)

    if not fm:
        return ("SKIP_NO_FRONTMATTER", "", "")

    if fm.get("is_template") is True:
        return ("SKIP_TEMPLATE", "", "")

    type_val = fm.get("type", "")
    if not type_val:
        return ("SKIP_NO_TYPE", "", "")

    area = clean_area(fm.get("area", ""))
    endpoint = get_endpoint_for_type(type_val, area)
    if not endpoint:
        return ("SKIP_UNKNOWN_TYPE", type_val, "")

    title = fm.get("title", "")
    if not title:
        return ("SKIP_NO_TITLE", "", "")

    builder = URL_BUILDERS[endpoint]
    new_url = builder(host, fm)
    if not new_url:
        return ("SKIP_NO_TITLE", "", "")

    current_url = fm.get("cover", "") or fm.get("og-image", "")

    if current_url == new_url:
        return ("NOOP", current_url, new_url)

    if apply:
        if backup and not str(path).endswith(".bak"):
            try:
                shutil.copy2(path, str(path) + ".bak")
            except Exception as e:
                return ("ERROR", current_url, f"backup error: {e}")

        new_content = update_frontmatter_og_image(content, new_url)
        if new_content == content:
            return ("ERROR", current_url, "no change after update")
        try:
            path.write_text(new_content, encoding="utf-8")
        except Exception as e:
            return ("ERROR", current_url, f"write error: {e}")
        return ("UPDATE" if current_url else "CREATE", current_url, new_url)

    return ("UPDATE" if current_url else "CREATE", current_url, new_url)


def main():
    parser = argparse.ArgumentParser(description="Apply og-image URLs to Obsidian vault notes.")
    parser.add_argument("--vault", default=".", help="Path to the Obsidian vault (default: current dir)")
    parser.add_argument("--host", default="https://og.sofian.lab", help="Base URL of the OG image service")
    parser.add_argument("--apply", action="store_true", help="Apply changes (default: dry-run)")
    parser.add_argument("--no-backup", action="store_true", help="Don't create .bak files before modifying")
    args = parser.parse_args()

    vault = Path(args.vault).resolve()
    if not vault.exists():
        print(f"Vault not found: {vault}", file=sys.stderr)
        sys.exit(1)

    host = args.host
    apply = args.apply
    backup = not args.no_backup

    mode = "APPLY" if apply else "DRY-RUN"
    print(f"=== {mode} ===")
    print(f"Vault: {vault}")
    print(f"Host:  {host}")
    print(f"Backup: {'no' if not backup else 'yes (.bak)'}")
    print()

    counts = {
        "UPDATE": 0,
        "CREATE": 0,
        "NOOP": 0,
        "SKIP_TEMPLATE": 0,
        "SKIP_NO_TYPE": 0,
        "SKIP_NO_TITLE": 0,
        "SKIP_NO_FRONTMATTER": 0,
        "SKIP_UNKNOWN_TYPE": 0,
        "ERROR": 0,
    }

    candidates = 0
    for root, dirs, files in os.walk(vault):
        # Skip .obsidian, node_modules, .git, .trash
        for skip in [".obsidian", "node_modules", ".git", ".trash", ".agents", ".opencode"]:
            if skip in dirs:
                dirs.remove(skip)
        # Skip 99-System/AI Handoffs (reference docs, not real notes)
        if "AI Handoffs" in root:
            continue

        for f in files:
            if not f.endswith(".md"):
                continue
            if f.endswith(".bak"):
                continue
            path = Path(root) / f
            try:
                rel = path.relative_to(vault)
            except ValueError:
                rel = path

            status, current, new = process_note(path, host, apply, backup)
            counts[status] = counts.get(status, 0) + 1

            if status in ("UPDATE", "CREATE"):
                candidates += 1
                rel_str = str(rel)[:80]
                if apply:
                    print(f"[{status:6}] {rel_str}")
                else:
                    print(f"[{status:6}] {rel_str}")
                    print(f"   new: {new[:150]}{'...' if len(new) > 150 else ''}")
            elif status == "ERROR":
                rel_str = str(rel)[:80]
                print(f"[{status:6}] {rel_str} — {new}")
            elif status == "SKIP_UNKNOWN_TYPE":
                if not apply:  # Only show unknowns in dry-run to avoid spam
                    rel_str = str(rel)[:60]
                    print(f"[{status:6}] {rel_str} (type={current!r})")

    print()
    print("=== Summary ===")
    for k, v in counts.items():
        if v > 0:
            print(f"  {k}: {v}")
    print(f"  Total candidates: {candidates}")

    if not apply and candidates > 0:
        print()
        print("Run with --apply to perform the changes.")


if __name__ == "__main__":
    main()
