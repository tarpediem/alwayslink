# ALS Odoo branding — design spec

**Date** : 2026-05-06
**Author** : Louise (assisted by Olivier)
**Status** : approved
**Implements** : module `als_branding` for the ALS Odoo 19 Enterprise instance on mamouth LXC 201

## 1. Problem

The default Odoo `external_layout_boxed` rendering of quotation S00001 is unfit for client delivery: the cyan `#7EE8FA` header is loud and off-brand, no logo is shown, customer name `Royi Sal` appears alone in the top-right, the totals box is a flat slab of cyan, and the body has zero typographic hierarchy. None of this aligns with the ALS brand kit (`design/brand/`).

## 2. Goal

Ship a versioned, deployable Odoo module that rebrands **all** company-issued documents (quotation, invoice, delivery slip, purchase order, payment receipt, picking) with the ALS brand identity:

- **Navy** `#0F1D31` for primary text and the footer band.
- **Cyan** `#1DA7E0` as accent only — never as flat fill behind text.
- **Grey** `#6B737B` for secondary text.
- Typography stack `Montserrat, Inter, "Helvetica Neue", Arial, sans-serif`.
- Logo `als-logo.svg` in the header, signature block, banking info Thailand in the footer.

The module installs cleanly, uninstalls cleanly, leaves no orphan records, and is deployed via `git pull` from GitHub on mamouth.

## 3. Non-goals

- Not a multi-company branding system. ALS company id=1 only.
- Not a theming engine — colors and font stack are hard-coded in SCSS, not user-configurable. Override in code if rebrand happens.
- No POS receipt customization (different rendering pipeline).
- No email template restyling (out of scope for v1; can be added later).
- No `l10n_th.report_invoice_document` deep override in v1 — the `external_layout_als` will style its frame, but Thai-tax-form fields stay as l10n_th renders them.

## 4. Architecture

### 4.1 Module location

```
alwayslink/odoo/addons/als_branding/
├── __manifest__.py
├── __init__.py
├── models/
│   ├── __init__.py
│   └── res_company.py
├── views/
│   ├── external_layout.xml
│   ├── report_saleorder.xml
│   └── res_company_views.xml
├── data/
│   └── res_company_data.xml
└── static/
    ├── description/
    │   └── icon.png
    └── src/
        ├── scss/
        │   └── als_report.scss
        └── img/
            └── als-mark-white.svg
```

### 4.2 Module manifest

- `depends`: `base`, `web`, `sale`, `account`
- `assets`: `web.report_assets_common` includes `als_branding/static/src/scss/als_report.scss`
- `auto_install`: false
- `application`: false (it's branding, not a feature app)
- `license`: `LGPL-3`

### 4.3 New QWeb templates

- `als_branding.external_layout_als` — full layout (header / body wrap / footer) registered as a selectable layout in `Settings > Companies > Document Layout`.
- `als_branding.als_report_layout_als` — entry in `report.layout` model (preview thumbnail, sequence) so it appears in the layout picker.

### 4.4 View overrides (xpath inherits)

- Inherits `sale.report_saleorder_document` to:
  - Restyle the document title block (`QUOTATION` badge in navy + `Sxxxxx` in cyan + valid-until date in grey).
  - Add a `Bill to:` / `Salesperson` two-column meta table.
  - Wrap the line table in a styled container so SCSS catches `.als-report` ancestor.
  - Append a `Terms & Conditions` and a `Signature` block when `require_signature=True`.

### 4.5 New fields on `res.company`

| Field | Type | Purpose |
|---|---|---|
| `als_bank_info` | `Text` | Bank name + account number + SWIFT printed in footer column 3. Plain text so user can format with line breaks. |
| `als_signatory_name` | `Char` | Full name printed under "For ALS" signature line. |
| `als_signatory_title` | `Char` | Job title printed under signatory name. |

All three are nullable and rendered with `t-if` guards so an empty value gracefully removes the corresponding block.

### 4.6 SCSS strategy

The SCSS file targets `.als-report` (the wrapper class added on `external_layout_als`). It declares CSS custom props for the brand colors at the top of the wrapper, then themes:

- `.als-report__header`: cyan top bar, logo + company info zone, document badge zone.
- `.als-report__customer`: bill-to card.
- `.als-report__meta`: 2-col meta table.
- `.als-report__lines`: table styling (navy header, light row separators, totals callout).
- `.als-report__sections`: styled section/note line variants.
- `.als-report__terms`: light grey terms box.
- `.als-report__signature`: 2-column signature block.
- `.als-report__footer`: full-width navy band, 3-col layout.

Font stack `Montserrat, Inter, "Helvetica Neue", Arial, sans-serif`. We attempt `@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600;700&display=swap')` but accept that wkhtmltopdf may fall back to system Helvetica/Arial. Since Montserrat is geometric sans-serif, the fallback is visually close.

## 5. Data flow

1. Module installed → `res_company_data.xml` runs (`noupdate=1`) → main company `als_signatory_name` defaults seeded if empty.
2. User opens `Settings > Companies > Document Layout` → picks "Always Link" from the layout list (preview thumbnail visible).
3. User triggers any report (`Print Quotation`, `Print Invoice`, etc.) → Odoo renders via `external_layout_als` → SCSS applies → wkhtmltopdf produces the branded PDF.

## 6. Error handling

- **Empty company logo**: external_layout falls back to `als-mark-white.svg` shipped in the module (placeholder).
- **Empty `als_bank_info` / `als_signatory_*`**: `t-if` guards remove the block silently.
- **`l10n_th.report_invoice_document` collision**: external_layout still wraps it, body content is l10n_th's. Acceptable for v1.
- **wkhtmltopdf fails to fetch Google Fonts**: SCSS font-stack falls back through Inter → Helvetica Neue → Arial. All system-available, render is acceptable.

## 7. Testing

### Pre-install
- `pg_dump -Fc alwayslinksolutions` → `/root/backups/als_pre_branding_<timestamp>.dump`. Required before `Apps > Install`.

### Post-install
- Open S00001, click `Print` → verify PDF downloads.
- Diff against the screenshot Olivier shared on 2026-05-06.
- Open invoice (when one exists) → verify l10n_th invoice still works (no XPath crash).
- Open delivery slip → verify external_layout_als applies (consistency check).

### Uninstall safety
- `Apps > als_branding > Uninstall` should leave company.layout reverted to whatever was set before (or to default boxed).
- New `als_*` fields on `res.company` removed without orphan data.

## 8. Deployment

```bash
# on mamouth
ssh mamouth
pct enter 201

# inside LXC 201
mkdir -p /opt/als && cd /opt/als
git clone https://github.com/tarpediem/alwayslink.git
chown -R odoo:odoo /opt/als

# patch /etc/odoo/odoo.conf — add line:
#   addons_path = /usr/lib/python3/dist-packages/odoo/addons,/opt/als/alwayslink/odoo/addons
# (or: keep default + append our path)

# backup before any module action
sudo -u postgres pg_dump -Fc alwayslinksolutions \
  > /root/backups/als_pre_branding_$(date +%Y%m%d-%H%M%S).dump

# restart odoo to pick up new addons_path
systemctl restart odoo

# install module via Apps menu (or XML-RPC button_immediate_install)
# pick layout in Settings > Companies > Document Layout
```

Update flow: `cd /opt/als/alwayslink && git pull && systemctl restart odoo` then `Apps > als_branding > Upgrade` (or XML-RPC `button_immediate_upgrade`).

## 9. Open questions deferred

- Banking info / signatory / phone number content → Olivier fills via `Settings > Companies` after install. Module ships fields empty.
- Multi-language report copy (TH/EN) → out of scope, current Odoo i18n covers it.
- Logo of the ALS company itself → Olivier should upload `design/brand/logo/als-logo.svg` to `Settings > Companies > Logo` if not already done.

## 10. Rollback plan

If the module misbehaves after install:

1. `Apps > als_branding > Uninstall` — non-destructive, leaves PG schema clean.
2. If uninstall fails: restore from PG dump via `dropdb alwayslinksolutions && createdb -O odoo alwayslinksolutions && pg_restore -d alwayslinksolutions /root/backups/als_pre_branding_<ts>.dump`.
3. `systemctl restart odoo`.
