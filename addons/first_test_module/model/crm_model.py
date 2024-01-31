
from odoo import api, fields, models

var = "asd"
def check_functon():
    pass
class CrmLead(models.Model):
    _inherit = "crm.lead" # inherit_ means model already exits
    #_name ='crm.lead' # thisis name of the obkect
    test_data =  fields.Char(
        string="Test Data y", 
        readonly=True)
    test_module =  fields.Char(
        string="Test Data y")
    event_types= fields.Many2one(
    comodel_name="event.types",
    string="event types")
    event_venues= fields.Many2one(
    comodel_name="event.venues",
    string="event venues")
    email_date= fields.Many2many(
    comodel_name="email.date",
    string="email date")
    total_people= fields.Many2many(
    comodel_name="total.people",
    string="total people")
    email_date= fields.Many2many(
    comodel_name="email.date",
    string="email date")



    def check_method(self):
        pass


'''

Class vs Objects 
class plane {
no_engines = 1 
no_wheels = 3 
function blow_wheel()
}

obj_plan = new plane(); memory and live on memory 
8086
JNE
JL
JE 


16 , 32 , 64 

16 , 32, 64 

do this ,  AABC 
do thata , A8b6
jump this ,



ob_plan2 = new plane();

function vs method
varriab;e vs propertiers 



'''