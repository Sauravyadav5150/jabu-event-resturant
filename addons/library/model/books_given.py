from odoo import api, fields, models

var = "asd"
def check_functon():
    pass
class booksgiven(models.Model): 
    _name ='books.given'   # create table "order_details" and connect to model order.details
    # this is name of the model  , and when you replace . with _ it becomes table name  
    # when its _name only , means create a new table , or change it 
    #_inherit ='order.details' 
    # name of an existing table , means take all columns from this table 
    # when _inherit!= _name  means take columns from _inherit table and create new table with _name as name
    # when you have only _inherit means change existing table using this class 

    name=fields.Char(
        string="books given") # create table "order_details" and connect to model order.details
    # this is name of the model  , and when you replace . with _ it becomes table name  
    # when its _name only , means create a new table , or change it 
    #_inherit ='order.details' 
    # name of an existing table , means take all columns from this table 
    # when _inherit!= _name  means take columns from _inherit table and create new table with _name as name
    # when you have only _inherit means change existing table using this class 

    name=fields.Char
  
   
    issue_date=  fields.Date(
        string="issue date" ) # create colimn 'issue date' 
                       #feild of type date  feild of type selection field.int means 
                       #  on the table order.details with
                       # with  Label 'issue date'
   
    
    return_date =  fields.Date(
        string="return date" )  # create colimn 'return_date' 
                       #feild of type  date  feild of type date field.date means 
                       #  on the table books.given with
                       # with  Label "return date"

    penalty=  fields.Float(
        string="penalty" )  # create colimn 'penalty' 
                       #feild of type  float  feild of type float field.float means 
                       #  on the table books.given with
                       # with  Label "penalty"

     
    

    book_id = fields.Many2one(
    comodel_name="library.books",
    string="Book")
                    # create colimn 'book_id' 
                    # feild of type  Many2one  feild of type FK field.Many2One means 
                    #  on the table books.given with
                    # with  Label "book id"
                    # connect to id column of table  "library.books"--  comodel_name="library.books"
                    # book_id to id of library books
 


    member_id = fields.Many2one(
    comodel_name="library.members",
    string="member id")
                    # create colimn 'member_id' 
                    # feild of type  Many2one  feild of type FK field.Many2One means 
                    #  on the table books.given with
                    # with  Label "member id"
                    # connect to id column of table  "library.member"--  comodel_name="library.member"
                    # member_id to id of library members
def check_method(self):
        pass