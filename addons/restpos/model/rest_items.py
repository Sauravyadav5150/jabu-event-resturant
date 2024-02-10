
from odoo import api, fields, models

var = "asd"
def check_functon():
    pass
class restitems(models.Model): 
    _name ='rest.items' # create table "rest_items" and connect to model rest.items
    # this is name of the model  , and when you replace . with _ it becomes table name  
    # when its _name only , means create a new table , or change it 
    #_inherit ='order.details' 
    # name of an existing table , means take all columns from this table 
    # when _inherit!= _name  means take columns from _inherit table and create new table with _name as name
    # when you have only _inherit means change existing table using this class 
    name=fields.Char(
            string="Item Name")
    price=fields.Float(
        string="price") # create colimn 'price' 
                       #feild of type Float  feild of type selection field.float means 
                       #  on the table rest.items with
                       # with  Label 'price'

    def check_method(self):
        pass