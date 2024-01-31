
from odoo import api, fields, models

var = "asd"
def check_functon():
    pass
class EventVenues(models.Model):
    _name ='event.venues' 
    name =  fields.Char(
        string="event venues" ) 
    

    def check_method(self):
        pass