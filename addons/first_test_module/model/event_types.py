
from odoo import api, fields, models

var = "asd"
def check_functon():
    pass
class EventTypes(models.Model):
    _name ='event.types' 
    name =  fields.Char(
        string="event types" ) 
    

    def check_method(self):
        pass