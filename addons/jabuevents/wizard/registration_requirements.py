from odoo import api, fields, models

class registrationrequirements(models.TransientModel):
    _name = 'registration.requirements'
    _description = 'all the details of event'

    registration_counter=fields.Boolean("string=registration counter")
    registration_staff=fields.Boolean(string="registration staff")
    # landyards=fields.text(string="landyards")
    # tshirts=fields.text(string="t-shirts")
   
    '''
    (
        'Closing Note', sanitize=True
    )
    '''

    def print_report(self):
        data = {
            'model': 'registration.requirements',
            'form': self.read()[0]
        }