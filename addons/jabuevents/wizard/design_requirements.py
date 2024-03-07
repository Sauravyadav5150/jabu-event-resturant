from odoo import api, fields, models

class designrequirements(models.TransientModel):
    _name = 'design.requirements'
    _description = 'all the info of design requiremnts'

    artwork = fields.Boolean(string='artwork')
    design=fields.Boolean(string="design")
  
    '''
    (
        'Closing Note', sanitize=True
    )
    '''

    def print_report(self):
        data = {
            'model': 'design.requirements',
            'form': self.read()[0]
        }