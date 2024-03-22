from odoo import api, fields, models

var = "asd"
def check_functon():
    pass
class sectionproduct(models.Model):
    _name ='section.product' 
    
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

    head_id = fields.Many2one(
    comodel_name="section.head",
    string="head id")
    
    

    def check_method(self):
        pass