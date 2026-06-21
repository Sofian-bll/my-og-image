<div align="center">

[![License: MIT](https://img.shields.io/github/license/Sofian-bll/my-og-image?style=flat)](https://github.com/Sofian-bll/my-og-image/blob/main/LICENSE)
[![Version](https://img.shields.io/github/v/release/Sofian-bll/my-og-image?style=flat)](https://github.com/Sofian-bll/my-og-image/releases)
[![Stars](https://img.shields.io/github/stars/Sofian-bll/my-og-image?style=flat)](https://github.com/Sofian-bll/my-og-image/stargazers)

<p align="center">
  <img src="docs/assets/logo.png" alt="my-og-image logo" width="160"/>
</p>

<a id="readme-top"></a>
<h1 align="center">my-og-image</h1>

<p align="center">Dynamic Open Graph image generator powered by Nuxt and the Takumi renderer.</p>

<p align="center">🇬🇧 <a href="README.md"><b>English</b></a> · 🇫🇷 <a href="README.fr.md">Français</a></p>

</div>

---

<p align="center">
  <a href="https://sofian-bll.github.io/my-og-image/"><strong>Explore the docs</strong></a>
  ·
  <a href="https://github.com/Sofian-bll/my-og-image/issues/new?labels=bug">Report Bug</a>
  ·
  <a href="https://github.com/Sofian-bll/my-og-image/issues/new?labels=enhancement">Request Feature</a>
</p>

<details open>
<summary>Table of Contents</summary>

- [What is this?](#what-is-this)
- [Features](#features)
- [How It Works](#how-it-works)
- [Demo](#demo)
- [Built With](#built-with)
- [Prerequisites](#prerequisites)
- [Quick Start](#quick-start)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Star History](#star-history)

</details>

## What is this?

my-og-image generates rich 1200×630 Open Graph images from Markdown frontmatter — turning Obsidian notes into polished social cards for Twitter, Discord, and link embeds. Built on [Nuxt 4](https://nuxt.com/) with the [Takumi renderer](https://github.com/hywax/takumi) and [nuxt-og-image](https://github.com/nuxt-modules/og-image), it serves eight dedicated template types through a single API endpoint.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Features

- **8 template types** — Aspiration, Epitech Project, Machine, Project, Resource, Service, System Config, Task — each with its own layout, gradient, and icon set
- **Takumi renderer** — type-driven, Satori-based layouts via `@takumi-rs/core`
- **Eyebrow config system** — auto-split titles on separators (` - `, ` — `, ` | `), surfacing context as a styled eyebrow badge
- **Context pills** — Lucide icons paired with location/context metadata (computer, school, home, etc.)
- **Obsidian vault sync** — Python script to batch-apply OG image URLs across every note in a vault
- **Docker-ready** — multi-stage build and compose files for local dev and production
- **Custom font** — Syne by Google Fonts, optimized for headings at multiple sizes

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## How It Works

```mermaid
graph LR
    A[Markdown Note] --> B[/api/og/:template]
    B --> C[Template Component]
    C --> D[Takumi Renderer]
    D --> E[nuxt-og-image]
    E --> F[1200x630 PNG]
    F --> G[Social Card]
```

A note's frontmatter (title, subtitle, tags, status, dates) is passed as query parameters to `/api/og/:template`. The matching Vue component assembles a Takumi layout, the renderer produces a PNG, and `nuxt-og-image` handles caching and response headers. Each template has its own gradient, icon palette, and typographic scale — all driven by the type config in `src/templates/`.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Demo

<p align="center">
  <img src="docs/assets/screenshot.png" alt="my-og-image landing page" width="800"/>
</p>

Visit the live landing page: [sofian-bll.github.io/my-og-image](https://sofian-bll.github.io/my-og-image/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Built With

- [![Nuxt](https://img.shields.io/badge/Nuxt-00DC82?style=flat&logo=nuxt.js&logoColor=white)](https://nuxt.com/) — Framework
- [![Vue.js](https://img.shields.io/badge/vuejs-%2335495e.svg?style=flat&logo=vuedotjs&logoColor=%234FC08D)](https://vuejs.org/) — UI framework
- [![TypeScript](https://img.shields.io/badge/typescript-%23007ACC.svg?style=flat&logo=typescript&logoColor=white)](https://www.typescriptlang.org/) — Language
- [![Node.js](https://img.shields.io/badge/node.js-6DA55F?style=flat&logo=node.js&logoColor=white)](https://nodejs.org/) — Runtime
- [![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=flat&logo=docker&logoColor=white)](https://www.docker.com/) — Containerization

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Prerequisites

- [Node.js](https://nodejs.org/) ≥ 18
- [pnpm](https://pnpm.io/) (lockfile is `pnpm-lock.yaml`)
- [Docker](https://www.docker.com/) (optional, for containerized deployment)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Quick Start

```bash
# Install dependencies
pnpm install

# Development server (http://localhost:3000)
pnpm dev
```

### Docker

```bash
# Production
docker compose up -d

# Development (hot reload)
docker compose -f docker-compose.dev.yml up -d
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Configuration

All settings live in `nuxt.config.ts`:

```ts
export default defineNuxtConfig({
  modules: ['nuxt-og-image', '@nuxt/fonts'],

  site: {
    url: 'https://og.sofian.lab',   // Your deployment URL
  },

  fonts: {
    families: [
      { name: 'Syne', weights: [400, 700], provider: 'google' },
    ],
  },

  ogImage: {
    renderer: 'takumi',
    defaults: {
      width: 1200,
      height: 630,
    },
  },
})
```

Template colors and eyebrow rules are configured in `src/templates/colors.ts` and `src/templates/eyebrow-config.ts`.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Usage

OG images are served at:

```
/api/og/:template?title=...&subtitle=...&tags=...&status=...
```

### Templates and Parameters

| Template | Key Parameters |
|----------|---------------|
| Aspiration | `title`, `subtitle`, `status`, `statusLabel`, `tags` |
| EpitechProject | `title`, `subtitle`, `status`, `tags`, `priority` |
| Machine | `title`, `subtitle`, `url`, `cover`, `status` |
| Project | `title`, `subtitle`, `status`, `url`, `tags` |
| Resource | `title`, `subtitle`, `status`, `type`, `tags` |
| Service | `title`, `subtitle`, `url`, `cover`, `status`, `tags` |
| SystemConfig | `title`, `subtitle`, `host`, `url` |
| Task | `title`, `subtitle`, `context`, `status`, `start`, `end`, `priority` |

### Quick Examples

```
/api/og/Resource?title=Design Systems - The Complete Guide&status=in_progress&type=Article&tags=design,systems,css
/api/og/Task?title=Set up CI/CD pipeline&context=school&status=todo&start=2026-03-01&priority=high
/api/og/Aspiration?title=Build a design system from scratch&status=paused&statusLabel=PAUSED
```

### Obsidian Automation

The `scripts/apply-og-images-homelab.py` script scans an Obsidian vault and writes OG image URLs into each note's frontmatter:

```bash
python scripts/apply-og-images-homelab.py /path/to/obsidian/vault --base-url https://your-domain.com
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Project Structure

```
assets/               Logo (PNG)
components/OgImage/   Template components (*.takumi.vue)
docs/                 Landing page + assets
scripts/              Vault sync utilities
server/api/og/        API endpoint ([template].get.ts)
src/templates/        Theme config (colors, eyebrow rules, icons)
app.vue               Root component
docker-compose.yml    Production compose
Dockerfile            Multi-stage build
nuxt.config.ts        Nuxt configuration
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contributing

Contributions are welcome. Open an issue to discuss what you'd like to change.

1. Fork the repo
2. Create a branch (`git checkout -b feature/amazing`)
3. Commit your changes (`git commit -m 'feat: add amazing thing'`)
4. Push to the branch (`git push origin feature/amazing`)
5. Open a Pull Request

<p align="center">
  <img src="https://contrib.rocks/image?repo=Sofian-bll/my-og-image" />
</p>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## License

MIT © 2026 Sofian — see [LICENSE](LICENSE) for details.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Star History

<p align="center">
  <a href="https://star-history.com/#Sofian-bll/my-og-image&Date">
    <img src="https://api.star-history.com/svg?repos=Sofian-bll/my-og-image&type=Date" alt="Star History Chart" width="600"/>
  </a>
</p>

---

<!-- REFERENCE_LINKS -->
[Nuxt]: https://nuxt.com/
[nuxt-og-image]: https://github.com/nuxt-modules/og-image
[Takumi renderer]: https://github.com/hywax/takumi
[@takumi-rs/core]: https://github.com/hywax/takumi
[Node.js]: https://nodejs.org/
[Docker]: https://www.docker.com/
[pnpm]: https://pnpm.io/
[Vue.js]: https://vuejs.org/
[TypeScript]: https://www.typescriptlang.org/
[Google Fonts]: https://fonts.google.com/
