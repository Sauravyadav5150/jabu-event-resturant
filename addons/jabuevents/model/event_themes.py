from odoo import api, fields, models

var = "asd"
def check_functon():
    pass
class eventhemes(models.Model): 
    _name ='event.themes'

    name=fields.Char(
      string="theme name")
    
    def check_method(self):
        pass
    