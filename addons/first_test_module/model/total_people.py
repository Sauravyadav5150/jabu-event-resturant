from odoo import api, fields, models

var = "asd"
def check_functon():
    pass
class TotalPeople(models.Model):
    _name ='total.people' 
    name =  fields.int(
        string="total people" ) 
    

    def check_method(self):     
        pass