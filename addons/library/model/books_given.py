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

    name=fields.char(
        string="books given")
    # name has to be explicitly created , with char , this field may not be needed for all tables 
   
    issue_date=  fields.date(
        string="issue date" ) # create colimn 'issue date' 
                       #feild of type date  feild of type selection field.int means 
                       #  on the table order.details with
                       # with  Label 'books given'
    # there is no need to create Id fields in odoo , since every model creates 5 fields by default 
    # ID , created_by,created_At,updated_by,updated_at
    
    
    return_date =  fields.date(
        string="return date" )  # create colimn 'return_date' 
                       #feild of type  date  feild of type date field.date means 
                       #  on the table books.given with
                       # with  Label "books given"

    penalty=  fields.float(
        string="penalty" )  # create colimn 'penalty' 
                       #feild of type  float  feild of type float field.float means 
                       #  on the table books.given with
                       # with  Label "books given"

     
    

book_id = fields.Many2one(
    comodel_name="library.books",
    string="book id")


member_id = fields.Many2one(
    comodel_name="library.members",
    string="member id")

def check_method(self):
        pass