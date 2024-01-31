
from odoo import api, fields, models

var = "asd"
def check_functon():
    pass
class restpayment(models.Model):
    _name ='rest.payment' 
    name =  fields.int(
        string="rest payment" ) 
      
    total_paid=fields.float(
        string="total paid")
    
    date_and_time=fields.datetime.now(
        string="date and time")
    
    order_id = fields.Many2one(
    comodel_name="order.table",
    string="order id")


    def check_method(self):
        pass