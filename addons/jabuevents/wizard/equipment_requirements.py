from odoo import api, fields, models

class equipmentrequirements(models.TransientModel):
    _name = 'equipment.requirements'
    _description = 'all the details of equipment requirements'

    light_equipments = fields.Boolean(string='light equipments')
    sound_equipments = fields.Boolean(string='sound equipments')
    av_equipements = fields.text(string='av equipments')
    tech_riders = fields.Boolean(string='tech rider')
   
    '''
    (
        'Closing Note', sanitize=True
    )
    '''

    def print_report(self):
        data = {
            'model': 'equipment.requirements',
            'form': self.read()[0]
        }