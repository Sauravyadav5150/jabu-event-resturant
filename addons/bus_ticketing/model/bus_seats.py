
from odoo import api, fields, models

var = "asd"
def check_functon():
    pass
class busseats(models.Model): 
    _name ='bus.seats'

    bus_id = fields.Many2one(
    comodel_name="bus.info",
    string="bus id")

    seat_no=fields.Integer(
      string="seat no")
    
    seat_price=fields.Float(
      string="seat price")

def check_method(self):
        pass


