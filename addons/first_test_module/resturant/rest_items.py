
from odoo import api, fields, models

var = "asd"
def check_functon():
    pass
class restitems(models.Model):
    _name ='rest.items' 
    name =  fields.Char(
        string="rest items" ) 
    

    def check_method(self):
        pass