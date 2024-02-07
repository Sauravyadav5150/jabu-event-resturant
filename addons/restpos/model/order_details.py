
from odoo import api, fields, models

var = "asd"
def check_functon():
    pass
class orderdetails(models.Model): 
    _name ='order.details'   # create table "order_details" and connect to model order.details
    # this is name of the model  , and when you replace . with _ it becomes table name  
    # when its _name only , means create a new table , or change it 
    #_inherit ='order.details' 
    # name of an existing table , means take all columns from this table 
    # when _inherit!= _name  means take columns from _inherit table and create new table with _name as name
    # when you have only _inherit means change existing table using this class 

                    
    name =  fields.Char(
        string="order details" ) 
    # name has to be explicitly created , with char , this field may not be needed for all tables 
    id= fields.Integer(
        string="id" ) 
                       # create colimn 'id' 
                       #feild of type  int  feild of type selection field.int means 
                       #  on the table order.details with
                       # with  Label 'order de'
    # there is no need to create Id fields in odoo , since every model creates 5 fields by default 
    # ID , created_by,created_At,updated_by,updated_at
    item_name=fields.Char(
      string="item name")
                       # create colimn 'item_name' 
                       #feild of type  char  feild of type char field.char means 
                       #  on the table order.details with
                       # with  Label "order details"
    item_price=fields.float(
      string="item price")
                       # create colimn 'item_name' 
                       #feild of type  float  feild of type float field.float means 
                       #  on the table order.details with
                       # with  Label "order details"
    item_id=fields.Many2one(
    comodel_name="rest.items",
    string="item id")
                    # create colimn 'item_id' 
                    # feild of type  One2Many  feild of type FK field.One2Many means 
                    #  on the table order.details with
                    # with  Label "item id"
                    # connect to id column of table  "rest.items"--  comodel_name="rest.items"
                    # item_id to id of order table 
 
    order_id = fields.Many2one(
    comodel_name="order.table",
    string="order id")



    quantity=fields.float(
        string="quantity")
'''

# id
# order_id
# item_id - foriegh key
# quantity
# price

how do i know which detail belongs to which order ?


'''

# is the code below this line needed if not delete it 





