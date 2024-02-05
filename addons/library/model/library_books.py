
from odoo import api, fields, models

var = "asd"
def check_functon():
    pass
class librarybooks(models.Model): 
    _name ='library.books' 
    name=fields.char(
        string="library books")

    title=  fields.char(
        string="title" ) # create colimn 'title' 
                       #feild of type  char  feild of type char field.char means 
                       #  on the table library.books with
                       # with  Label "title"
    
    author= fields.char(
        string="Author" ) # create colimn 'author' 
                       #feild of type  char  feild of type char field.char means 
                       #  on the table library.books with
                       # with  Label "author"
    
    edition= fields.int(
        string="Edition" )# create colimn 'edition' 
                       #feild of type  int  feild of type int field.int means 
                       #  on the table library.books with
                       # with  Label "edition"

    year_published= fields.int(
        string="Year published" )# create colimn 'year_published' 
                       #feild of type  int  feild of type char field.int means 
                       #  on the table library.books with
                       # with  "year published"

    id= fields.int(
        string="total copies" ) # create colimn 'total_copies' 
                       #feild of type  int  feild of type int field.int means 
                       #  on the table library.books with
                       # with  Label "total copies"

    
    def check_method(self):
        pass

  