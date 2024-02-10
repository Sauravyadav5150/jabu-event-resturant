
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

                    
    
    item_price=fields.Float(
      string="item price")
                       # create colimn 'item_price' 
                       #feild of type  float  feild of type float field.float means 
                       #  on the table order.details with
                       # with  Label "item price"
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
    string="order id")  # create colimn 'order_id'  
                    # feild of type  Many2one  feild of type FK field.Many2one means 
                    #  on the table order.details with
                    # with  Label "order id"
                    # connect to id column of table  "order.table"--  comodel_name="order.table"
                    # item_id to id of order table 



    quantity=fields.Float(
        string="quantity")
    line_total =fields.Float(
        string="Line Total" )
    
    @api.onchange('quantity')
    def _compute_line_total(self):
        self.line_total = self.quantity * self.item_price
        pass
'''

# id
# order_id
# item_id - foriegh key
# quantity
# price




'''

# is the code below this line needed if not delete it 





