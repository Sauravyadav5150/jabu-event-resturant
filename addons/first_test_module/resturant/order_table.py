
from odoo import api, fields, models

var = "asd"
def check_functon():
    pass
class ordertable(models.Model):
    _name ='order.table' 
    name =  fields.Char(
        string="order table" ) 
    

    def check_method(self):
        pass