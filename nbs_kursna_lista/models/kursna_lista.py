import requests
from datetime import datetime
from odoo import models, fields, api

class CurrencyRateUpdateNBS(models.Model):
    _inherit = 'res.currency'

    def update_currency_rate(self):
        url = "https://api.nbs.rs/public/kursnaLista"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            for item in data:
                currency_code = item['currency_code']
                rate = item['middle_rate']

                currency = self.env['res.currency'].search(['name', '=', currency_code], limit=1)
                if currency:
                    self.env['res.currency.rate'].create({
                        'currency_id': currency.id,
                        'rate': 1/ rate,
                        'name': datetime.now(),
                    })