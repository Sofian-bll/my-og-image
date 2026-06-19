> [Read in English](README.md) | [Lire en Francais](README.fr.md)

<p align="center">
  <img src="assets/logo.svg" alt="og-image logo" width="160"/>
</p>

<h1 align="center" id="readme-top">og-image</h1>

<p align="center">
  Dynamic Open Graph image generator powered by Nuxt and the Takumi renderer.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/license-MIT-blue?style=flat" alt="License"/>
  <img src="https://img.shields.io/badge/Nuxt-4.x-00DC82?style=flat&logo=nuxt.js" alt="Nuxt"/>
  <img src="https://img.shields.io/badge/Docker-ready-2496ED?style=flat&logo=docker" alt="Docker"/>
</p>

---

## What is this?

og-image generates rich Open Graph preview images for social sharing and link embeds. Built on Nuxt with the Takumi renderer and `nuxt-og-image`, it renders eight dedicated template components from markdown frontmatter — turning Obsidian-style metadata into polished 1200×630 social cards.

## Features

- **8 template types** — Aspiration, Epitech Project, Machine, Project, Resource, Service, System Config, Task
- **Takumi renderer** — produces clean, type-driven layouts via `@takumi-rs/core`
- **Obsidian sync** — scripts to batch-apply OG URLs across an entire vault
- **Docker-ready** — multi-stage build + compose for deployment
- **Custom font** — Syne by Google Fonts, optimized for headings

## Built With

- [Nuxt 4](https://nuxt.com/) — framework
- [nuxt-og-image](https://github.com/nuxt-modules/og-image) — OG image module
- [@takumi-rs/core](https://github.com/hywax/takumi) — image renderer
- [Docker](https://www.docker.com/) — containerization

## Quick Start

```bash
# Install dependencies
pnpm install

# Development server
pnpm dev

# Production build
pnpm build
pnpm start
```

### Docker

```bash
docker compose up -d
```

The app runs on `http://localhost:3000`.

OG images are served at `/api/og/[template]` with query parameters (see the Obsidian scripts for the full URL schema).

## Project Structure

```
assets/          Logo
components/      Takumi template components (OgImage/*.takumi.vue)
scripts/         Vault sync utilities (apply-og-images.py)
server/api/og/   API endpoint ([template].get.ts)
src/templates/   Theme config (colors, eyebrow labels)
```

## License

MIT © 2026 Sofian — see [LICENSE](LICENSE).
