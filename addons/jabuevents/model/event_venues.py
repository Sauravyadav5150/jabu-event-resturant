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
    
    event_details = fields.One2many( "event.details", "venues_id", string="Event details")
    
    def check_method(self):
        pass
    


 