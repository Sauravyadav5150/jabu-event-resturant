
from odoo import api, fields, models

var = "asd"
def check_functon():
    pass
class busguests(models.Model): 
    _name ='bus.guest'

    phone_no=fields.Integer(
      string="phone number")

    address=fields.Char(
      string="address") 
    
    def check_method(self):
        pass
    
