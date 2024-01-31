
from odoo import api, fields, models

var = "asd"
def check_functon():
    pass
class CrmLead(models.resturant):
    _inherit = "crm.lead" # inherit_ means model already exits
    #_name ='crm.lead' # thisis name of the obkect
    test_data =  fields.Char(
        string="Test Data y", 
        readonly=True)
    test_module =  fields.Char(
        string="Test Data y")
    order_details= fields.Many2one(
    comodel_name="order.details",
    string="order details")
    order_table= fields.Many2one(
    comodel_name="order.table",
    string="order table")
    rest_items= fields.Many2many(
    comodel_name="rest.items",
    string="rest items")
    total_people= fields.Many2many(
    comodel_name="rest.payment",
    string="rest payment")
   


    def check_method(self):
        pass