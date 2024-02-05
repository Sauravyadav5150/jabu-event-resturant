
from odoo import api, fields, models

var = "asd"
def check_functon():
    pass
class librarybooks(models.Model): 
    _name ='library.books' 
    name=fields.char(
        string="library books")

    name =  fields.char(
        string="title" ) 
    
    id= fields.char(
        string="Author" ) 
    
    id= fields.int(
        string="Edition" )

    id= fields.int(
        string="Year published" )

    id= fields.int(
        string="total copies" ) 

    
    def check_method(self):
        pass

  