from odoo import api, fields, models
import logging
_logger = logging.getLogger(__name__)

class createevents(models.TransientModel):
    _inherit =  'create.events' 

    fields_list_to_parse = ["event_info_type_of_event","event_info_event_date_start1","event_info_event_date_end1","event_info_destination",
"event_info_event_venue_s_","event_info_no_of_pax","event_info_events_s_details_event_info",
"event_info_themes","dmc_requirements_airport_transfers","dmc_requirements_airport_rep_service",
"dmc_requirements_ground_transportation","dmc_requirements_accommodation_sourcing",
"dmc_requirements_venue_sourcing","dmc_requirements_excursions","design_requirements_artwork",
"design_requirements_design ","registration_requirements_registration_counter",
"registration_requirements_registration_staff","registration_requirements_id_lanyards",
"registration_requirements_t_shirts ","equipment_requirements_light_equipment",
"equipment_requirements_sound_equipment","equipment_requirements_led_av_equipment",
"equipment_requirements_tech_riders_required  ","photo_video_requirements_photo",
"photo_video_requirements_video","photo_video_requirements_highlight_video_edit",
"photo_video_requirements_ob_set_up ","production_branding_standees",
"production_branding_registration_branding","production_branding_backdrops",
"production_branding_photowall","production_branding_photobooth",
"production_branding_stage_branding","production_branding_printing",
"production_branding_stage_rental","production_branding_carpet","production_branding_stairs",
"production_branding_d_cor ","photobooth_standard_photobooth_backdrop_only",
"photobooth_standard_photobooth_images_print","photobooth_360_photobooth_gifs",
"photobooth_glambot_photobooth_gifs ","others_misc_requirements_gifts",
"others_misc_requirements_furniture_rental","others_misc_requirements_hybrid_uplink_service",
"others_misc_requirements_trophy_awards","others_misc_requirements_podium",
"others_misc_requirements_translation  ","entertainment_thai_theme",
"entertainment_tech_led","entertainment_band_musicians_dj","entertainment_dance",
"entertainment_ambient","entertainment_cirque ","activities_team_building",
"activities_cruise","manpower_emcee","manpower_hostesses","manpower_ushers",
"manpower_models","manpower_security","manpower_event_staff","manpower_interpreter",
"manpower_labor","manpower_delivery"]

    def clean_name(self,name):
        if name[0]=='_':
            return name[1:]
        else:
            return name

    def get_sections(self):
        output_list = list(map(self.clean_name, self.total_state))
        return output_list


    def createPartner(self):
        partner = self.env['res.partner']
        return partner.create({
            "name":self.client_name
        })
    

    def convert_to_sale_order(self):
        order = self.env["sale.order"]
        lines = self.createLines()
        partner = self.createPartner()
        order.create({
            "partner_id":partner.id,
            "order_line":lines,
        })

    def createLines(self):
        lines = []
        
        sections = self.get_sections()
        _logger.error(sections)
        for each in sections:
            if each == "event_info":
                continue
            fields = self.getFields(each)
            
            for field_raw in fields:
                field = field_raw.strip()
                fieldType = self.getType(field)
                value = self.getValue(field)
                data = self.createLine(field,fieldType,value)
                _logger.error("%s %s %s"%(field,fieldType,each))
                if data != None:
                    lines.append(data)

                
        return lines 
    def getType(self,field):
        ir_model_obj=self.env['ir.model.fields']
        ir_model_field=ir_model_obj.search([('model','=',["create.events"]),('name','=',field)])
        return ir_model_field.ttype
    def getValue(self,value):
        return self.__getattribute__(value) 
    def createLine(self,field,fieldType,value):
        if fieldType == 'boolean' and type(value)==type(True):
            if value ==True:
                return (0,0,{"name":field,'display_type':"line_section"})
        if fieldType == "text" and type(value)==type("s"):
            if value.strip() != "":
                return (0,0,{"name":field+" __ "+value,'display_type':"line_section"})
        return None
                

    def getFields(self,each):
            fields= [item for item in self.fields_list_to_parse if item.startswith(each)]
            _logger.error(fields)
            return fields
    
    # def open_next(self):
    #     self.convert_to_sale_order()
    #     pass

  


        