from odoo import api, fields, models

class eventdetails(models.TransientModel):
    _name = 'event.details'
    _description = 'all the details of event'

    themes_id = fields.Many2many('event.themes', string='themes')
    venues_id = fields.Many2one('event.venues', 'venues')(
        'Closing Note', sanitize=True
    )