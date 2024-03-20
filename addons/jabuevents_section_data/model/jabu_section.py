from odoo import api, fields, models

var = "asd"
def check_functon():
    pass
class jabusection(models.Model):
    _name ='jabu.section' 
    
    section_name=fields.Char(
        string="section name")
    
    section_description=fields.Text(
        string="section description")
    
    priority=fields.Integer(
        string="priority")
    
    products = fields.One2many( "jabu.products", "product_id", string="all the types of product")
        


    def check_method(self):
        pass