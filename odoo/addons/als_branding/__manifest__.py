# -*- coding: utf-8 -*-
{
    "name": "ALS Branding",
    "version": "19.0.1.0.0",
    "summary": "Always Link Solutions — branded report layout (quotation, invoice, delivery)",
    "description": """
Always Link Solutions branding pack
====================================

Adds a custom external_layout (`Always Link`) used by every printable
document Odoo emits: sale orders, invoices, delivery slips, purchase
orders, payment receipts, pickings.

Includes:
- New external layout `als_branding.external_layout_als` with brand-correct
  navy / cyan / grey palette and Montserrat typography.
- Override of `sale.report_saleorder_document` for production-grade quotations.
- Three new fields on `res.company` for footer banking info and signatory.
- SCSS injected through `web.report_assets_common`.
""",
    "author": "Always Link Solutions",
    "website": "https://alwayslinksolutions.com",
    "category": "Customizations",
    "license": "LGPL-3",
    "depends": [
        "base",
        "web",
        "sale",
        "account",
    ],
    "data": [
        "views/external_layout.xml",
        "views/report_saleorder.xml",
        "views/res_company_views.xml",
        "data/report_layout_data.xml",
    ],
    "assets": {
        "web.report_assets_common": [
            "als_branding/static/src/scss/als_report.scss",
        ],
    },
    "images": [
        "static/description/icon.png",
    ],
    "installable": True,
    "auto_install": False,
    "application": False,
}
