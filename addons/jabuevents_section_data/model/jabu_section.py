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
    
    product_id = fields.Many2one(
    comodel_name="jabu.product",
    string="product id")

        


    def check_method(self):
        pass