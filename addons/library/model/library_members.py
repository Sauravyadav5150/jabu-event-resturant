
from odoo import api, fields, models

var = "asd"
def check_functon():
    pass
class librarymembers(models.Model): 
    _name ='library.members' 
    name=fields.char(
        string="library members")
    
    name=fields.char(
        string="name")
    
    contact_no=fields.int(
        string="contact no")
    
    address=fields.char(
        string="address")
    
    def check_method(self):
        pass

