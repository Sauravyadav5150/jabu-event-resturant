from odoo import api, fields, models

class evententertainment(models.TransientModel):
    _name = 'event.entertainment'
    _description = 'all the details of dmc'

    thai_theme = fields.text(string='thai theme')
    tech_led=fields.text(string="tech/led")
    brand=fields.text(string="brand/musicians/dj")
    dance=fields.text(string="dance")
    ambient=fields.text(string="ambient")
    cirque=fields.text(string="cirque")
 
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