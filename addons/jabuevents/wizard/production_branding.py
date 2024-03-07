from odoo import api, fields, models

class productionbranding(models.TransientModel):
    _name = 'production.branding'
    _description = 'details about production and branding'

    standees = fields.Boolean(string='standees')
    registration_branding = fields.Boolean(string='registration branding')
    backdrops = fields.Boolean(string='backdrops')
    photowall = fields.Boolean(string='photowall')
    photobooth = fields.Boolean(string='photobooth')
    stage_branding = fields.Boolean(string='stage branding')
    printing = fields.Boolean(string='printing')
    stage_rental = fields.Boolean(string='stage rental')
    carpet=fields.Boolean(string="carpet")
    stairs=fields.Boolean(string="stairs")
    decor = fields.Boolean(string='decor')
    '''
    (
        'Closing Note', sanitize=True
    )
    '''

    def print_report(self):
        data = {
            'model': 'production.branding',
            'form': self.read()[0]
        }