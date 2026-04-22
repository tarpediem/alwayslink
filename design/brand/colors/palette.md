# Charte couleur — Always Link Solutions

## Primaires

| Rôle | Hex | RGB | Usage |
|---|---|---|---|
| **Navy** | `#0F1D31` | `15, 29, 49` | Symbole principal, typographie "ALWAYS LINK", backgrounds sombres, corps de texte |
| **Cyan** | `#1DA7E0` | `29, 167, 224` | Accent (le petit "A" dans le triangle), liens, CTAs, highlights |

## Secondaires

| Rôle | Hex | RGB | Usage |
|---|---|---|---|
| **Grey** | `#6B737B` | `107, 115, 123` | Sous-titre "SOLUTIONS", texte secondaire, séparateurs |
| **White** | `#FFFFFF` | `255, 255, 255` | Fond clair, logo inversé sur navy |

## Déclinaisons suggérées (à confirmer avec un tool de contraste)

- Navy sombre (pressed state) : `#0A1324`
- Navy clair (hover/border) : `#1A2D4B`
- Cyan sombre (pressed) : `#1791C4`
- Cyan clair (hover) : `#49B8E6`
- Grey sombre : `#4F5660`
- Grey clair : `#9CA3AB`

## Format CSS custom properties

```css
:root {
  --als-navy: #0F1D31;
  --als-cyan: #1DA7E0;
  --als-grey: #6B737B;
  --als-white: #FFFFFF;

  --als-navy-dark: #0A1324;
  --als-navy-light: #1A2D4B;
  --als-cyan-dark: #1791C4;
  --als-cyan-light: #49B8E6;
  --als-grey-dark: #4F5660;
  --als-grey-light: #9CA3AB;
}
```

## Format Tailwind (config)

```js
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        als: {
          navy:    { DEFAULT: '#0F1D31', dark: '#0A1324', light: '#1A2D4B' },
          cyan:    { DEFAULT: '#1DA7E0', dark: '#1791C4', light: '#49B8E6' },
          grey:    { DEFAULT: '#6B737B', dark: '#4F5660', light: '#9CA3AB' },
        },
      },
    },
  },
}
```

## Contraste (WCAG)

| Couleur texte | Fond | Ratio | AA | AAA |
|---|---|---|---|---|
| Navy `#0F1D31` | White `#FFFFFF` | ~17:1 | ✅ | ✅ |
| White `#FFFFFF` | Navy `#0F1D31` | ~17:1 | ✅ | ✅ |
| Cyan `#1DA7E0` | White `#FFFFFF` | ~2.9:1 | ❌ | ❌ |
| Cyan `#1DA7E0` | Navy `#0F1D31` | ~5.8:1 | ✅ (texte normal AA) | ❌ |
| Grey `#6B737B` | White `#FFFFFF` | ~4.7:1 | ✅ (AA) | ❌ |

**À retenir** :
- Ne jamais utiliser **cyan sur blanc pour du texte** — réservé aux gros titres ou aux accents graphiques.
- Le grey passe AA uniquement pour texte large (>18pt / >14pt bold).
- Pour petits textes sur fond blanc, toujours utiliser navy.
