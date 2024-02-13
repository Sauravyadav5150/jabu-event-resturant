
from odoo import api, fields, models

var = "asd"
def check_functon():
    pass
class bustickets(models.Model): 
    _name ='bus.tickets'

    bus_id = fields.Many2one(
    comodel_name="bus.info",
    string="bus id")

    guest_id = fields.Many2one(
    comodel_name="bus.guest",
    string="guest id")

    seat_id = fields.Many2one(
    comodel_name="bus.seats",
    string="seat id")

    deperature=fields.Char(
      string="deperature")
    
    destination=fields.Char(
      string="destination")
    
    total_price=fields.Float(
      string="total price")

    def check_method(self):
        pass
    
    




    