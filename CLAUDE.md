# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project scope

Umbrella repository for **Always Link Solutions (ALS)** — IT consulting focused on DevOps, AI automation, and business systems for SME in Southeast Asia.

This is **not** a single-app codebase. It hosts multiple subprojects:

- `design/logos/` — monochrome SVG logos of the tools we work with (brand-neutral, `fill="currentColor"`)
- `design/logos-color/` — the same set in brand colors (for pitch decks, slides, brochures)
- Future: website source, infrastructure-as-code, marketing assets, documentation

## Subproject conventions

- Each subproject has its own README / manifest — read *that* first before editing.
- Add new subprojects as top-level directories (`web/`, `infra/`, `docs/`, …).
- Client-specific work lives in separate repos or gitignored subdirectories — **not** here.

## Working rules

- **`*.local.md` is gitignored** — use it for anything environment-specific (internal IPs, infra notes, drafts).
- **Deployment**: pull from GitHub on target servers. No direct scp/rsync.
- **Language**: user-facing copy in English by default. Code comments in English.

## Licensing

- Code / documentation in this repo → MIT (see `LICENSE`).
- Third-party logos redistributed in `design/logos*/` retain their original licenses — see `design/logos/README.md` and `NOTICE`.
