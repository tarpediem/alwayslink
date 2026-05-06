# -*- coding: utf-8 -*-
from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    als_bank_info = fields.Text(
        string="Bank info (footer)",
        help="Bank name, account number, SWIFT — printed in the third "
             "footer column of branded reports. Plain text with line breaks.",
    )
    als_signatory_name = fields.Char(
        string="Signatory name",
        help="Name printed under the 'For ALS' signature box on quotations "
             "that require a signature.",
    )
    als_signatory_title = fields.Char(
        string="Signatory title",
        help="Job title printed under the signatory name.",
    )
