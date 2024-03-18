from odoo import api, fields, models

var = "asd"
def check_functon():
    pass
class jabuproduct(models.Model):
    _name ='jabu.product' 
    
    product_name=fields.Char(
        string="product name")
    
    product_description=fields.Text(
        string="product description")
    
    quantity=fields.Integer(
        string="quantity")
    
    price=fields.Float(
        string="price")
    
    manufacturer=fields.Char(
        string="manufacturer")
    
    section_id = fields.Many2one(
    comodel_name="jabu.section",
    string="section id")

    
    

    def check_method(self):
        pass