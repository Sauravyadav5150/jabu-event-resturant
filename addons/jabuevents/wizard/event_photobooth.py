from odoo import api, fields, models

class eventphotobooth(models.TransientModel):
    _name = 'event.photobooth'
    _description = 'all the details of event'

    photobooth_backdrop = fields.Boolean(string='photobooth backdrop')
    photobooth_images=fields.Boolean(string="photobooth images")
    photobooth_gif=fields.Boolean(string="360 photobooth")
    glambot_photobooth=fields.Boolean(string="glambot photobooth")
    
    '''
    (
        'Closing Note', sanitize=True
    )
    '''

    def print_report(self):
        data = {
            'model': 'event.photobooth',
            'form': self.read()[0]
        }