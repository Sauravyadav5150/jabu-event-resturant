from odoo import api, fields, models

class dmcrequirements(models.TransientModel):
    _name = 'dmc.requirements'
    _description = 'all the details of dmc'

    airport_transfers = fields.Boolean(string='airport transfer')
    airport_rep=fields.Boolean(string="airport rep service")
    ground_transportation=fields.Boolean(string="ground transport")
    accommodation_sourcing=fields.Boolean(string="accommodation sourcing")
    venue_sourcing=fields.Boolean(string="venue sourcing")
    excursion=fields.Boolean(string="excursion")
 
    '''
    (
        'Closing Note', sanitize=True
    )
    '''

    def print_report(self):
        data = {
            'model': 'dmc.requirements',
            'form': self.read()[0]
        }