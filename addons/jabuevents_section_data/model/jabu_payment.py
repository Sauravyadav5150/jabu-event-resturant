from odoo import api, fields, models

var = "asd"
def check_functon():
    pass
class jabupayment(models.Model):
    _name ='jabu.payment' 
    
    amount=fields.Int(
        string="product amount")
    
    payment_date=fields.Date(
        string="payment date")
    
    product_id = fields.Many2one(
    comodel_name="jabu.product",
    string="product id")

    
    

    def check_method(self):
        pass