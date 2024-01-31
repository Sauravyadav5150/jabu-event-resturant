
from odoo import api, fields, models

var = "asd"
def check_functon():
    pass
class orderdetails(models.Model): 
    _name ='order.details' 
    name =  fields.int(
        string="order details" ) 
    

    def check_method(self):
        pass