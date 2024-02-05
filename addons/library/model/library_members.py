
from odoo import api, fields, models

var = "asd"
def check_functon():
    pass
class librarymembers(models.Model): 
    _name ='library.members' 
    name=fields.char(
        string="library members")
    
    member_name=fields.char(
        string="member name") # create colimn 'member_name' 
                       #feild of type  char  feild of type char field.char means 
                       #  on the table library.members with
                       # with  Label "member name"
    
    contact_no=fields.int(
        string="contact no")# create colimn 'contact_no' 
                       #feild of type  int  feild of type int field.int means 
                       #  on the table library.members with
                       # with  Label "contact no"
    
    address=fields.char(
        string="address")# create colimn 'address' 
                       #feild of type  char  feild of type char field.char means 
                       #  on the table library.members with
                       # with  Label "address"
    
    def check_method(self):
        pass

