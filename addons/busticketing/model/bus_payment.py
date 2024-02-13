
from odoo import api, fields, models

var = "asd"
def check_functon():
    pass
class buspayment(models.Model): 
    _name ='bus.payment'

    ticket_id = fields.Many2one(
    comodel_name="bus.tickets",
    string="ticket id")

    payment_amount=fields.Float(
      string="payment amount")

    method=fields.Char(
      string="method")
    

    def check_method(self):
        pass



