from odoo import api, fields, models

var = "asd"
def check_functon():
    pass
class booksgiven(models.Model): 
    _name ='books.given' 
    name=fields.char(
        string="books given")
    
    date =  fields.date(
        string="issue date" ) 
    
    
    name =  fields.date(
        string="return date" )

    penalty=  fields.float(
        string="penalty" ) 
     
    

book_id = fields.Many2one(
    comodel_name="library.books",
    string="book id")


member_id = fields.Many2one(
    comodel_name="library.members",
    string="member id")

def check_method(self):
        pass