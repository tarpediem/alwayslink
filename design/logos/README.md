# Logos — stack Always Link Solutions

Deux collections miroir sous `design/` :

| Dossier | Fichiers | Style | Cas d'usage |
|---|---|---|---|
| `logos/` | 204 SVG | **Monochrome** (simple-icons) | Web : `fill="currentColor"` dans CSS pour coloriser dynamiquement, dark/light mode |
| `logos-color/` | 229 SVG | **Couleurs officielles** (Homarr + devicon + simple-icons branded) | Pitch decks, slides client, brochures — respect du brand kit de chaque outil |

Même arborescence dans les deux. Pour la plupart des logos, `logos-color/<x>.svg` a les couleurs natives de la marque ; pour les quelques irréductibles (fish, Firecrawl, pgvector, Acronis), `logos-color/` contient un fallback monochrome identique à `logos/`.

## Sources

| Source | URL | Licence | Utilisé pour |
|---|---|---|---|
| **simple-icons** | https://github.com/simple-icons/simple-icons | CC0 1.0 | `logos/` (mono), `logos-color/` via `cdn.simpleicons.org/<slug>/<hex>` |
| **dashboard-icons (Homarr)** | https://github.com/homarr-labs/dashboard-icons | CC0 1.0 | `logos-color/` (couleur native) + quelques ajouts mono |
| **devicon** | https://github.com/devicons/devicon | MIT | `logos-color/` dev tools (Python, FastAPI, Git, Nginx, etc.) |
| **selfhst/icons** | https://github.com/selfhst/icons | CC BY-SA 4.0 | Fallback pour self-hosting |
| **Waydroid** | https://github.com/waydroid/waydroid.github.io | Logo officiel du projet | `tools/waydroid*.svg` |

> ⚠️ Les logos restent la propriété de leurs titulaires de marque. simple-icons/homarr sont CC0 mais les **marques déposées** (Proxmox, NVIDIA, Anthropic, etc.) obéissent à leurs propres guidelines d'usage. Pour un usage commercial dans une comm ALS (pitch deck, site, brochure), vérifier le brand kit officiel du concerné.

## Arborescence

```
design/logos{,-color}/
├── ai/                 (8)   → Ollama, Anthropic, Claude, ClaudeAI, OpenAI, HuggingFace,
│                              OpenRouter, OpenWebUI
├── automation/         (2)   → n8n, Zapier
├── backup/             (2)   → OpenZFS, Proxmox Backup Server
├── build/             (10)   → Vite, Webpack, Rollup, esbuild, Parcel, Turbo, SWC, Babel,
│                              Gulp, Grunt
├── business/           (6)   → Odoo, Mailcow, Nextcloud, OnlyOffice, WordPress, SOGo
├── ci-cd/             (11)   → GitHub Actions, GitLab CI, Jenkins, CircleCI, Drone, Woodpecker,
│                              Argo, Tekton, Ansible, Terraform, Pulumi
├── cloud/             (21)   → AWS (+EC2/S3), GCP, Azure, DigitalOcean, Hetzner, Vercel, Netlify,
│                              Cloudflare Pages/Workers, Hostinger, Linode, Vultr, OVH, Scaleway,
│                              Railway, Render, Fly, Firebase, Supabase
├── databases/          (7)   → PostgreSQL, Redis, Neo4j, SQLite, MongoDB, MySQL, ChromaDB
├── dev/                (22)  → Python, FastAPI, Git, GitHub, GitLab, fish, Bash, Node, Bun,
│                              TS, JS, Rust, Go, Deno, Ruby, PHP, Elixir, .NET, C, C++, Kotlin, Zig
├── devtools/          (33)   → Neovim, Vim, Emacs, tmux, Helix, Zed, Starship, ripgrep, Hyper,
│                              WezTerm, Alacritty, Ghostty, iTerm2, Warp, zsh, PowerShell, curl,
│                              wget, Postman, Insomnia, HTTPie, Bruno, jq, YAML, JSON, Markdown,
│                              GitKraken, Sourcetree, Lazygit, Lazydocker, Figma, Mermaid, Excalidraw
├── frameworks/        (21)   → React, Vue, Svelte, Next.js, Nuxt, Astro, Remix, Solid, Qwik,
│                              SvelteKit, TailwindCSS, shadcn/ui, Radix UI, htmx, Alpine.js,
│                              Express, NestJS, Hono, Flask, Django, Gin
├── hardware/           (4)   → NVIDIA, AMD, Intel, DJI
├── infra/              (7)   → Proxmox, Docker, Docker Compose, Kubernetes, Portainer,
│                              Kasm, Kasm Workspaces
├── mcp-protocol/      (17)   → OpenAI, Anthropic, Gemini, Mistral, Grok, Groq, Perplexity,
│                              Cohere, HuggingFace, LangChain, LlamaIndex, Replicate, RunPod,
│                              Together, Fireworks, Windsurf, Cursor
├── network/            (8)   → Tailscale, Nginx, NPM, Cloudflare, OPNsense, pfSense,
│                              WireGuard, OpenVPN
├── os/                 (8)   → Linux, Arch, CachyOS, Ubuntu, Debian, GNOME, Wayland, Android
├── package-managers/  (12)   → npm, pnpm, yarn, uv, PyPI, pip, Cargo, Homebrew, AUR, pacman,
│                              Flatpak, Snapcraft
├── self-hosting/       (7)   → qBittorrent, Jellyfin, Jellyseerr, Radarr, Sonarr, Prowlarr,
│                              Home Assistant
├── testing/           (10)   → Playwright, Puppeteer, Cypress, Jest, Vitest, Mocha, pytest,
│                              Selenium, k6, Storybook
└── tools/             (13)   → VSCode, Obsidian, Firefox, Chrome, Thunderbird, Telegram, Slack,
                              Discord, RustDesk, SearXNG, Waydroid, Notion
```

## Manquants (pas de SVG officiel trouvé)

Ces outils n'ont pas de logo SVG disponible publiquement sur simple-icons / Homarr / repos GitHub. À récupérer manuellement si besoin :

- **Acronis** — brand kit officiel sur https://www.acronis.com/en-us/brand/ (demande d'accès)
- **Firecrawl** — uniquement en PNG sur le repo `mendableai/firecrawl`
- **pgvector** — pas de logo officiel, le projet est du SQL pur
- **Proxmox Backup Server** — utiliser `infra/proxmox.svg` (même branding)
- **MobiPOS** — pas de brand kit public
- **WinBoat** — projet trop récent, pas encore de logo
- **LXC** — utiliser `infra/docker.svg` ou `os/linux.svg` comme proxy visuel
- **SOGo, ROCm, CachyOS, MinisForum** — pas de SVG officiel dispo

## Usages typiques pour ALS

- **Pitch deck** : section "Tech stack" → piocher 8-12 logos représentatifs (Proxmox, Docker, Ollama, n8n, Odoo, PostgreSQL, Python, FastAPI…)
- **Site web `alwayslink.com`** : bandeau "Technologies we work with" avec grille de logos
- **Propositions client** : section credentials avec les outils maîtrisés
- **Slides BOI / investisseurs** : montrer la profondeur de la stack IT consulting

## Notes

- Tous les SVG sont monochromes sauf mention contraire (convention simple-icons). Utiliser `fill="currentColor"` dans le HTML/CSS pour le coloriser dynamiquement.
- `tools/waydroid-white.svg` est la version haute résolution officielle (264 KB, couleur) — réservée aux usages grand format.
- Ajouts futurs : créer la sous-catégorie manquante si besoin, et mettre à jour ce README.
