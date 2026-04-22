# ALS Brand Assets

Assets de marque officiels pour **Always Link Solutions**. Distinct de `design/logos/` qui contient les logos de technos tierces.

## Arborescence

```
design/brand/
├── logo/
│   ├── als-logo-full.png      → Logo source (PNG, 1536×1024, référence)
│   ├── als-logo.svg           → Logo complet avec texte, en couleurs (navy + cyan + grey)
│   ├── als-logo-mono.svg      → Logo complet, monochrome navy (tout en #0F1D31)
│   ├── als-logo-white.svg     → Logo complet, 100% blanc (pour fond foncé)
│   ├── als-logo-black.svg     → Logo complet, 100% noir (print / single-color)
│   ├── als-mark.svg           → Symbole uniquement, couleurs (pour favicon, avatar)
│   ├── als-mark-mono.svg      → Symbole monochrome navy
│   └── als-mark-white.svg     → Symbole blanc (fond foncé)
└── colors/
    ├── palette.md             → Charte couleur documentée (CSS, Tailwind, WCAG)
    └── palette.svg            → Visualisation de la palette
```

## Quand utiliser quoi

| Variant | Cas d'usage |
|---|---|
| `als-logo.svg` | Site web light mode, factures, pitch deck, slides pro |
| `als-logo-mono.svg` | Quand le cyan ne passe pas (impressions éco, monochrome, fond coloré) |
| `als-logo-white.svg` | Dark mode, slides sur fond navy, vêtements sombres, signature email dark |
| `als-logo-black.svg` | Tampons, faxes, impressions single-ink, gravures |
| `als-mark.svg` | Favicon couleur, avatar social (256×256+), watermark |
| `als-mark-mono.svg` | Favicon simple, loader, icône app |
| `als-mark-white.svg` | Icône sur fond navy, intro animation dark |

## Règles d'usage

- **Taille minimale** : 40px de haut pour `als-mark-*`, 120px de haut pour `als-logo-*` (sinon le texte devient illisible).
- **Safe zone** : laisser au moins 1× la hauteur du symbole de marge autour du logo.
- **Ne pas** : distordre les proportions, changer les couleurs, séparer les éléments du symbole, ajouter des effets (ombre, outline, gradient).
- **Fond coloré non-brand** : utiliser la version `-white` si le fond est foncé (>50% luminosité inversée), `-mono` si le fond est clair mais pas blanc.

## Couleurs

Voir [`colors/palette.md`](./colors/palette.md) pour la charte complète + snippets CSS/Tailwind.

**Raccourci** :
- Navy `#0F1D31` (primaire, marque)
- Cyan `#1DA7E0` (accent)
- Grey `#6B737B` (secondaire)
- White `#FFFFFF` (inverse)

## Typographie

Le logo utilise une sans-serif géométrique bold pour "ALWAYS LINK" et regular pour "SOLUTIONS". Les SVG référencent en fallback : `Montserrat, Inter, Helvetica Neue, Arial, sans-serif`.

Pour cohérence visuelle sur les supports ALS, utiliser **Montserrat** (Google Fonts, libre) comme font principale :
- `Montserrat 700` → titres, CTA, logo
- `Montserrat 400` → body text
- `Montserrat 300` → light variations

## Source & vectorisation

- Logo original fourni en PNG (1536×1024) le 2026-04-22.
- Vectorisation effectuée par `potrace` (séparation par masque couleur : navy via fuzz 25% sur #0F1D31, cyan via fuzz 8% sur #1DA7E0).
- Texte reconstitué en SVG `<text>` natif (pas un glyphe tracé) pour permettre édition et adaptation de la font.

Si Olivier obtient plus tard un fichier vectoriel source (Illustrator, Figma, Canva), le swap est trivial — remplacer les 3 fichiers `als-logo.svg` / `als-mark.svg` / `als-logo-full.png` par les nouveaux exports.
