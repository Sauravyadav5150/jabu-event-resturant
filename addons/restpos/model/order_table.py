
from odoo import api, fields, models

var = "asd"
def check_functon():
    pass
class ordertable(models.Model):
    _name ='order.table' 
    #no need to create table for id and created at
   

    status=fields.Char(
        string="status")
    
    order_no=fields.Integer(
        string="oder no")
    

    total_amount=fields.Float(
        string="total amount")
    

    def check_method(self):
        pass

        done