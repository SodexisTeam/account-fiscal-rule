# Copyright (C) 2009-TODAY Akretion <http://www.akretion.com>
#   @author Sébastien BEAU <sebastien.beau@akretion.com>
#   @author Renato Lima <renato.lima@akretion.com>
# Copyright 2012-TODAY Camptocamp SA
#   @author: Guewen Baconnier
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import fields, models


class AccountFiscalPositionRuleTemplate(models.Model):
    _name = "account.fiscal.position.rule.template"
    _description = "Account Fiscal Position Rule Template"
    _order = "sequence"

    name = fields.Char(string="Name", required=True)

    description = fields.Char(string="Description")

    from_country = fields.Many2one(comodel_name="res.country", string="Country Form")

    from_state = fields.Many2one(
        comodel_name="res.country.state",
        string="State From",
        domain="[('country_id','=',from_country)]",
    )

    to_invoice_country = fields.Many2one(
        comodel_name="res.country", string="Country To"
    )

    to_invoice_state = fields.Many2one(
        comodel_name="res.country.state",
        string="State To",
        domain="[('country_id','=',to_invoice_country)]",
    )

    to_shipping_country = fields.Many2one(
        comodel_name="res.country", string="Destination Country"
    )

    to_shipping_state = fields.Many2one(
        comodel_name="res.country.state",
        string="Destination State",
        domain="[('country_id','=',to_shipping_country)]",
    )

    fiscal_position_id = fields.Many2one(
        comodel_name="account.fiscal.position.template",
        string="Fiscal Position",
        required=True,
    )

    use_sale = fields.Boolean(string="Use in sales order")

    use_invoice = fields.Boolean(string="Use in Invoices")

    use_purchase = fields.Boolean(string="Use in Purchases")

    use_picking = fields.Boolean(string="Use in Picking")

    date_start = fields.Date(
        string="Start Date", help="Starting date for this rule to be valid."
    )

    date_end = fields.Date(
        string="End Date", help="Ending date for this rule to be valid."
    )

    sequence = fields.Integer(
        string="Priority",
        required=True,
        default=10,
        help="The lowest number will be applied.",
    )

    vat_rule = fields.Selection(
        selection=[
            ("with", "With VAT number"),
            ("both", "With or Without VAT number"),
            ("without", "Without VAT number"),
        ],
        string="VAT Rule",
        default="both",
        help=(
            "Choose if the customer need to have the"
            " field VAT fill for using this fiscal position"
        ),
    )
