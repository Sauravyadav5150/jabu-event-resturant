
from odoo import api, fields, models

var = "asd"
def check_functon():
    pass
class indooroutdoorselection(models.Model):
    _name ='indoor.outdoor.selection' 
    name =  fields.selection(
        string="indoor outdoor selection" ) 
    

    def check_method(self):
        pass