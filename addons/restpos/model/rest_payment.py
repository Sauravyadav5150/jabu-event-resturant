
from odoo import api, fields, models

var = "asd"
def check_functon():
    pass
class restpayment(models.Model):
    _name ='rest.payment' 
    name =  fields.int(
        string="rest payment" ) 
      
    item_price=fields.float(
        string="item price")

    

    def check_method(self):
        pass