from odoo import api, fields, models

var = "asd"
def check_functon():
    pass
class eventvenues(models.Model): 
    _name ='event.venues'

    name=fields.Char(
      string="venue name")
    
    destination=fields.Char(
      string="destination")
    
    def check_method(self):
        pass
    


 