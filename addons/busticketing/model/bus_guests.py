
from odoo import api, fields, models

var = "asd"
def check_functon():
    pass
class busguests(models.Model): 
    _name ='bus.guests'

    name=fields.Char(
      string="guest Name")
    
    phone_no=fields.Integer(
      string="phone number")

    address=fields.Char(
      string="address") 
    
    def check_method(self):
        pass
    
