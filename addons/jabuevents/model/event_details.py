from odoo import api, fields, models

var = "asd"
def check_functon():
    pass
class eventdetails(models.Model): 
    _name ='event.details'

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
    


