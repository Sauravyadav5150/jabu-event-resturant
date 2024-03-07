from odoo import api, fields, models

class miscrequirements(models.TransientModel):
    _name = 'misc.requirements'
    _description = 'all the details of event'

    gifts = fields.tex(string='gifts')
    furniture_rental=fields.Boolean(string="furniture rental")
    hybrid_uplink=fields.text(string="hybrid uplink")
    trophy=fields.Boolean(string="trophy")
    podium=fields.text(string="podium")
    translation = fields.text(string='translation')
    '''
    (
        'Closing Note', sanitize=True
    )
    '''

    def print_report(self):
        data = {
            'model': 'misc.requirements',
            'form': self.read()[0]
        }