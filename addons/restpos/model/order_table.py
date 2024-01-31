
from odoo import api, fields, models

var = "asd"
def check_functon():
    pass
class ordertable(models.Model):
    _name ='order.table' 
    name =  fields.Char(
        string="order table" )   
    # create colimn 'item_name' 
                       #feild of type  char  feild of type char field.char means 
                       #  on the table order.details with
                       # with  Label "order details"
    
    
    detail_ids = fields.One2many( "order.details",'order_id',string="orders id")
    

    status=fields.char(
        string="status")
    
    order_no=fields.Integer(
        string="oder no")
    

    total_amount=fields.float(
        string="total amount")
    

    def check_method(self):
        pass