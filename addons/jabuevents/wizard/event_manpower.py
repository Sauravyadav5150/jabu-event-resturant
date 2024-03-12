from odoo import api, fields, models

class eventmanpower(models.TransientModel):
    _name = 'event.manpower'
    _description = 'all the details of dmc'

    emcee = fields.Text(string='emcee')
    hostess=fields.Boolean(string="hostess")
    ushers=fields.Boolean(string="ushers")
    models=fields.Boolean(string="models")
    security=fields.Boolean(string="security")
    event_staff=fields.Boolean(string="event staff")
    interpreter=fields.Boolean(string="interpreter")
    labor=fields.Boolean(string="labor")
    delivery=fields.Boolean(string="delivery")
 
    '''
    (
        'Closing Note', sanitize=True
    )
    '''

    def print_report(self):
        data = {
            'model': 'event.manpower',
            'form': self.read()[0]
        }