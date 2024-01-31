
from odoo import api, fields, models

var = "asd"
def check_functon():
    pass
class restitems(models.Model):
    _name ='rest.items' 
    name =  fields.Char(
        string="Name of Item" )  
    price=fields.float(
        string="item price")

    def check_method(self):
        pass