
from odoo import api, fields, models

var = "asd"
def check_functon():
    pass
class businfo(models.Model): 
    _name ='bus.info'

    deperature_point=fields.Char(
      string="deperature point")
    
    destination_point=fields.Char(
      string="destination point")
    
    deperature_date=fields.Date(
      string="deperature date")
    
    arrival_date=fields.Date(
      string="arrival date")
    
    duration=fields.Float(
      string="duration")
    
    total_seats=fields.Integer(
      string="total seats")
    
    def check_method(self):
        pass
    
