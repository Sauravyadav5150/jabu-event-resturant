from odoo import api, fields, models

class evententertainment(models.TransientModel):
    _name = 'event.entertainment'
    _description = 'all the details of dmc'

    thai_theme = fields.Text(string='thai theme')
    tech_led=fields.Text(string="tech/led")
    band=fields.Text(string="brand/musicians/dj")
    dance=fields.Text(string="dance")
    ambient=fields.Text(string="ambient")
    cirque=fields.Text(string="cirque")
 
    '''
    (
        'Closing Note', sanitize=True
    )
    '''

    def print_report(self):
        data = {
            'model': 'event.entertainment',
            'form': self.read()[0]
        }