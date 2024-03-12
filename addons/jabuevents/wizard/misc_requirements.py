from odoo import api, fields, models

class miscrequirements(models.TransientModel):
    _name = 'misc.requirements'
    _description = 'all the details of event'

    gifts = fields.Text(string='gifts')
    furniture_rental=fields.Boolean(string="furniture rental")
    hybrid_uplink=fields.Text(string="hybrid uplink")
    trophy=fields.Boolean(string="trophy")
    podium=fields.Text(string="podium")
    translation = fields.Text(string='translation')
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