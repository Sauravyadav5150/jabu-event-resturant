
from odoo import api, fields, models

var = "asd"# variable 
def check_functon():
    pass
class Saleorder(models.Model):
    _inherit = "sale.order" # inherit_ means model already exits
    #_name ='crm.lead' # thisis name of the obkect/table 
    test_at = ";asdasd" #property 
    event_details =  fields.Char(
        string="Event details", 
        readonly=True) # colimn on the table crm.lead with name test_data 
                       #, field.Char means feild of type character
    name=fields.Char(
      string="event name")
    
    event_type=fields.Char(
      string="event type")

    event_date=fields.Date(
      string="event date")
    
    venues_id = fields.Many2one(
    comodel_name="event.venues",
    string="venues id")

    themes_id = fields.Many2one(
    comodel_name="event.themes",
    string="themes id")

    no_of_pax=fields.Integer(
      string="no of pax")

    def check_method(self):
        pass
    

