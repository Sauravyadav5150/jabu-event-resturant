from odoo import api, fields, models

class createevents(models.TransientModel):
    _name = 'create.events'
    _description = 'all the details of event'

    event_id = fields.Many2many('event.details', string='details')
    event_date=fields.Date(string="event date")
    event_destination=fields.Char(string="event destination")
    venues_id = fields.Many2one('event.venues', 'venues')(
        'Closing Note', sanitize=True
    )

    def print_report(self):
        data = {
            'model': 'create.events',
            'form': self.read()[0]
        }