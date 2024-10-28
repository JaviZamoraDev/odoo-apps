from odoo import fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    extra_fields = fields.Char(string="Extra")