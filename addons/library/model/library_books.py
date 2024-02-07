
from odoo import api, fields, models

var = "asd"
def check_functon():
    pass
class librarybooks(models.Model): 
    _name ='library.books' 
    name=fields.Char(
        string="library books")

    title=  fields.Char(
        string="title" ) # create colimn 'title' 
                       #feild of type  char  feild of type char field.char means 
                       #  on the table library.books with
                       # with  Label "title"
    
    author= fields.Char(
        string="Author" ) # create colimn 'author' 
                       #feild of type  char  feild of type char field.char means 
                       #  on the table library.books with
                       # with  Label "author"
    
    edition= fields.Integer(
        string="Edition" )# create colimn 'edition' 
                       #feild of type  int  feild of type int field.int means 
                       #  on the table library.books with
                       # with  Label "edition"

    year_published= fields.Integer(
        string="Year published" )# create colimn 'year_published' 
                       #feild of type  int  feild of type char field.int means 
                       #  on the table library.books with
                       # with  "year published"

    total_copies= fields.Integer(
        string="total copies" ) # create colimn 'total_copies' 
                       #feild of type  int  feild of type int field.int means 
                       #  on the table library.books with
                       # with  Label "total copies"

def check_method(self):
     pass

  
