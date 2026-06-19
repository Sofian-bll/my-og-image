> [Read in English](README.md) | [Lire en Francais](README.fr.md)

<p align="center">
  <img src="assets/logo.svg" alt="logo og-image" width="160"/>
</p>

<h1 align="center" id="readme-top">og-image</h1>

<p align="center">
  Generateur d'images Open Graph dynamiques, propulse par Nuxt et le renderer Takumi.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/license-MIT-blue?style=flat" alt="License"/>
  <img src="https://img.shields.io/badge/Nuxt-4.x-00DC82?style=flat&logo=nuxt.js" alt="Nuxt"/>
  <img src="https://img.shields.io/badge/Docker-ready-2496ED?style=flat&logo=docker" alt="Docker"/>
</p>

---

## C'est quoi ?

og-image genere des images de preview Open Graph pour le partage sur les reseaux sociaux et les embeds de liens. Construit sur Nuxt avec le renderer Takumi et `nuxt-og-image`, il transforme les metadonnees de type Obsidian en cartes sociales soignees de 1200×630 pixels.

## Fonctionnalites

- **8 templates** — Aspiration, Projet Epitech, Machine, Projet, Ressource, Service, Config Systeme, Tache
- **Renderer Takumi** — layouts propres et types via `@takumi-rs/core`
- **Sync Obsidian** — scripts pour appliquer les URLs OG sur un vault entier
- **Pret pour Docker** — build multi-etapes + compose pour le deploiement
- **Police personnalisee** — Syne via Google Fonts, optimisee pour les titres

## Stack technique

- [Nuxt 4](https://nuxt.com/) — framework
- [nuxt-og-image](https://github.com/nuxt-modules/og-image) — module OG image
- [@takumi-rs/core](https://github.com/hywax/takumi) — renderer d'images
- [Docker](https://www.docker.com/) — containerisation

## Demarrage rapide

```bash
# Installer les dependances
pnpm install

# Serveur de developpement
pnpm dev

# Build production
pnpm build
pnpm start
```

### Docker

```bash
docker compose up -d
```

L'application tourne sur `http://localhost:3000`.

Les images OG sont servies a `/api/og/[template]` avec des parametres de requete (voir les scripts Obsidian pour le schema d'URL complet).

## Structure du projet

```
assets/          Logo
components/      Composants template Takumi (OgImage/*.takumi.vue)
scripts/         Utilitaires de sync vault (apply-og-images.py)
server/api/og/   Point d'API ([template].get.ts)
src/templates/   Configuration du theme (couleurs, labels)
```

## Licence

MIT © 2026 Sofian — voir [LICENSE](LICENSE).
