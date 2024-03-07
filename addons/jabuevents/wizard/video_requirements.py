from odoo import api, fields, models

class videorequirements(models.TransientModel):
    _name = 'video.requirements'
    _description = 'all the details of vido and photography'

    photo = fields.Boolean(string='photo')
    video=fields.Boolean(string="video")
    highlight_video_edit=fields.Boolean(string="highlight video edit")
    ob_setup = fields.text(string='ob setup')
    '''
    (
        'Closing Note', sanitize=True
    )
    '''

    def print_report(self):
        data = {
            'model': 'video.requirements',
            'form': self.read()[0]
        }