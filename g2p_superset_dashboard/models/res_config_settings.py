import re

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    superset_url = fields.Char(
        string="Superset URL",
        config_parameter="g2p_superset_dashboard.superset_url",
    )

    def check_url(self, url):
        url_pattern = re.compile(
            r"^(?:http[s]?://)?(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+$",
            re.IGNORECASE,
        )
        if not url_pattern.match(url):
            error_msg = "Invalid URL format. Please use a valid URL."
            raise ValidationError(error_msg)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            superset_url_value = vals.get("superset_url")
            if superset_url_value:
                self.check_url(superset_url_value)
                self.env["ir.config_parameter"].sudo().set_param(
                    "g2p_superset_dashboard.superset_url", superset_url_value
                )

        result = super().create(vals_list)
        return result
