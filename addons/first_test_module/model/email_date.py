
from odoo import api, fields, models

var = "asd"
def check_functon():
    pass
class EmailDate(models.Model):
    _name ='email.date' 
    name =  fields.Date(
        string="email date" ) 
    

    def check_method(self):
        pass