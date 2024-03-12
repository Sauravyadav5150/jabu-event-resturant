from odoo import api, fields, models

class eventactivities(models.TransientModel):
    _name = 'evet.activities'
    _description = 'all the details of dmc'

    team_building = fields.Text(string='team building')
    cruise=fields.Boolean(string="cruise")
   
    '''
    (
        'Closing Note', sanitize=True
    )
    '''

    def print_report(self):
        data = {
            'model': 'event.activities',
            'form': self.read()[0]
        }