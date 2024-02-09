
from odoo import api, fields, models

var = "asd"
def check_functon():
    pass
class restpayment(models.Model):
    _name ='rest.payment' 
    
    total_paid=fields.Float(
        string="total paid")
    
    order_date=fields.Date(
        string="order date")
    
    details_id = fields.One2many(
    comodel_name="order.details",
    string="details id")


    def check_method(self):
        pass