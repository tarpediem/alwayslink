# Landing page Always Link Solutions

Single-file HTML landing générée par **Claude Design** (Anthropic Labs) le 2026-04-22. Trois langues :

| Langue | Path | Size |
|---|---|---|
| 🇫🇷 Français | [`fr/index.html`](./fr/index.html) | 23.5 KB |
| 🇬🇧 English | [`en/index.html`](./en/index.html) | 23.4 KB |
| 🇹🇭 ภาษาไทย | [`th/index.html`](./th/index.html) | 26.3 KB |

Chaque fichier est **autonome** : CSS inline, aucune dépendance locale. Seuls les fonts Google (Fraunces, Manrope, JetBrains Mono, IBM Plex Sans Thai pour la version TH) sont chargés via CDN.

## Preview local

```bash
# Serve le dossier, ouvre http://localhost:8080/fr/
python3 -m http.server 8080 --directory web/landing

# Ou avec bun / npx
npx serve web/landing -l 8080
```

## Charte utilisée

⚠️ **Divergence avec la charte officielle ALS** (`design/brand/colors/palette.md`) : Claude Design a choisi une palette **dark mode** propre, pas les navy/cyan officiels du logo.

| Rôle | Hex Claude Design | Notes |
|---|---|---|
| `--bg` | `#0A0C10` | Quasi-noir (plus sombre que le navy ALS) |
| `--bg-2` | `#0E1117` | Navy-black secondaire |
| `--ink` | `#F2F3F5` | Blanc cassé (texte principal) |
| `--ink-mute` | `#8A8F98` | Gris texte secondaire |
| `--ink-dim` | `#555A63` | Gris très discret |
| `--accent` | `#7EE8FA` | Cyan électrique (accents, liens) |
| `--accent-2` | `#3A6FF8` | Bleu profond (CTAs) |
| `--warm` | `#E8C9A0` | Touche chaude (sparingly) |

**Fonts** : Fraunces (serif, titres), Manrope (sans, body), JetBrains Mono (code), IBM Plex Sans Thai (TH uniquement).

## Réconciliation charte : à décider

Deux options :

1. **Aligner Claude Design sur la charte officielle** — swap `#0A0C10` → `#0F1D31` (navy), `#7EE8FA` → `#1DA7E0` (cyan). Plus fidèle au logo, moins "trendy".
2. **Garder la version Claude Design** et **mettre à jour la charte** — la palette Claude Design est plus riche (warm accent, multiple blues) et plus "agence digitale moderne".

Recommandation : décider avec Olivier avant de déployer publiquement sur `alwayslink.com`.

## Déploiement

Hosting statique minimal suffit. Options :
- **Cloudflare Pages** — zéro config, SSL auto, CDN mondial. Push → déploie.
- **Vercel / Netlify** — idem.
- **zenglow VPS** (Hostinger) — servir via Nginx dans `/var/www/alwayslink/`.

Quand alwayslink.com est enregistré, structure DNS recommandée :
- `alwayslink.com` → redirect vers `/en/` (marché SEA B2B → anglais par défaut)
- `fr.alwayslink.com` ou `alwayslink.com/fr/` → version FR
- `th.alwayslink.com` ou `alwayslink.com/th/` → version TH

## Sources

- Produit : [Claude Design (Anthropic Labs)](https://www.anthropic.com/news/claude-design-anthropic-labs) lancé 2026-04-17
- Fichiers source : ZIP export Claude Design (`als.zip`), extraits tels quels
