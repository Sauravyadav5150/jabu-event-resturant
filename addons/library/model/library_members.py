
from odoo import api, fields, models

var = "asd"
def check_functon():
    pass
class librarymembers(models.Model): 
    _name ='library.members' 
    name=fields.Char(
        string="library members")
    
    member_name=fields.Char(
        string="member name") # create colimn 'member_name' 
                       #feild of type  char  feild of type char field.char means 
                       #  on the table library.members with
                       # with  Label "member name"
    
    contact_no=fields.Integer(
        string="contact no")# create colimn 'contact_no' 
                       #feild of type  int  feild of type int field.int means 
                       #  on the table library.members with
                       # with  Label "contact no"
    
    address=fields.Char(
        string="address")# create colimn 'address' 
                       #feild of type  char  feild of type char field.char means 
                       #  on the table library.members with
                       # with  Label "address"
    
    given_books = fields.One2many( "books.given", "member_id", string="Books Taken")

    # 'sale.order.line', 'order_id', string='Order Lines'
    
def check_method(self):
     pass

#the above module works properly