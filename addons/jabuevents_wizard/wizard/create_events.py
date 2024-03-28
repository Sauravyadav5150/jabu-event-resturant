from odoo import api, fields, models
import logging

class createevents(models.TransientModel):
    _name = 'create.events' 

    total_state = ["client_info",
                    "_event_info",
                    "_dmc_requirements",
                    "_design_requirements",
                    "_registration_requirements",
                    "_equipment_requirements",
                    "_photo_video_requirements",
                    "_production_branding",
                    "_photobooth",
                    "_others_misc_requirements",
                    "_entertainment",
                    "_manpower"]

    _description = 'all the details of event'
    _selection_state = [('client_info','client_info'),
            ('_event_info','_event_info'),
            ('_dmc_requirements','_dmc_requirements'),
            ('_design_requirements','_design_requirements'),
            ('_registration_requirements','_registration_requirements'),
            ('_equipment_requirements','_equipment_requirements'),
            ('_photo_video_requirements','_photo_video_requirements'),
            ('_production_branding','_production_branding'),
            ('_photobooth','_photobooth'),
            ('_others_misc_requirements','_others_misc_requirements'),
            ('_entertainment','_entertainment'),
            ('_manpower','_manpower'),
            ("final","final")]

    state = fields.Selection(selection=_selection_state,string="state",default="client_info")
    client_name=fields.Text(string='Client Name')
    company=fields.Text(string='Company')
    company_address=fields.Text(string='Company Address')
    registration_tax_id=fields.Text(string='Registration / TAX ID')
    email_address=fields.Text(string='Email Address')
    mobile=fields.Text(string='Mobile')
    line_whatsapp_insta_fb=fields.Text(string='LINE / WhatsApp / Insta / FB')
    website=fields.Text(string='Website')


    event_info_type_of_event=fields.Selection(string='Type of Event',selection=[("corporate","Corporate"),("private","Private"),("wedding","Wedding")])
    event_info_event_date_start1=fields.Date(string='Event Date start')
    event_info_event_date_end1=fields.Date(string='Event Date end')
    event_info_destination=fields.Text(string='Destination')
    event_info_event_venue_s_=fields.Text(string='Event Venue(s)')
    event_info_no_of_pax=fields.Text(string='No of PAX')
    event_info_events_s_details_event_info=fields.Text(string='Events(s) Details - Event Info')
    event_info_themes=fields.Text(string='Themes')


    dmc_requirements_airport_transfers=fields.Boolean(string='Airport Transfers')
    dmc_requirements_airport_rep_service=fields.Boolean(string='Airport Rep Service')
    dmc_requirements_ground_transportation=fields.Boolean(string='Ground Transportation')
    dmc_requirements_accommodation_sourcing=fields.Boolean(string='Accommodation Sourcing')
    dmc_requirements_venue_sourcing=fields.Boolean(string='Venue Sourcing')
    dmc_requirements_excursions=fields.Boolean(string='Excursions')


    design_requirements_artwork=fields.Boolean(string='Artwork')
    design_requirements_design=fields.Boolean(string='Design')


    registration_requirements_registration_counter=fields.Boolean(string='Registration Counter')
    registration_requirements_registration_staff=fields.Boolean(string='Registration Staff')
    registration_requirements_id_lanyards=fields.Text(string='ID & Lanyards')
    registration_requirements_t_shirts=fields.Text(string='T-Shirts')


    equipment_requirements_light_equipment=fields.Boolean(string='Light Equipment')
    equipment_requirements_sound_equipment=fields.Boolean(string='Sound Equipment')
    equipment_requirements_led_av_equipment=fields.Text(string='LED / AV Equipment')
    equipment_requirements_tech_riders_required=fields.Boolean(string='Tech Riders Required')


    photo_video_requirements_photo=fields.Boolean(string='Photo')
    photo_video_requirements_video=fields.Boolean(string='Video')
    photo_video_requirements_highlight_video_edit=fields.Boolean(string='Highlight Video Edit')
    photo_video_requirements_ob_set_up=fields.Text(string='OB Set-up')


    production_branding_standees=fields.Boolean(string='Standees')
    production_branding_registration_branding=fields.Boolean(string='Registration Branding')
    production_branding_backdrops=fields.Boolean(string='Backdrops')
    production_branding_photowall=fields.Boolean(string='Photowall')
    production_branding_photobooth=fields.Boolean(string='Photobooth')
    production_branding_stage_branding=fields.Boolean(string='Stage Branding')
    production_branding_printing=fields.Boolean(string='Printing')
    production_branding_stage_rental=fields.Boolean(string='Stage Rental')
    production_branding_carpet=fields.Boolean(string='Carpet')
    production_branding_stairs=fields.Boolean(string='Stairs')
    production_branding_d_cor=fields.Boolean(string='Décor')



    photobooth_standard_photobooth_backdrop_only=fields.Boolean(string='Standard Photobooth Backdrop Only')
    photobooth_standard_photobooth_images_print=fields.Boolean(string='Standard Photobooth Images / Print')
    photobooth_360_photobooth_gifs=fields.Boolean(string='360 Photobooth GIFs')
    photobooth_glambot_photobooth_gifs=fields.Text(string='Glambot Photobooth GIFs')


    others_misc_requirements_gifts=fields.Text(string='Gifts')
    others_misc_requirements_furniture_rental=fields.Boolean(string='Furniture Rental')
    others_misc_requirements_hybrid_uplink_service=fields.Text(string='Hybrid Uplink Service')
    others_misc_requirements_trophy_awards=fields.Boolean(string='Trophy / Awards')
    others_misc_requirements_podium=fields.Boolean(string='Podium')
    others_misc_requirements_translation=fields.Text(string='Translation')


    entertainment_thai_theme=fields.Text(string='Thai Theme')
    entertainment_tech_led=fields.Text(string='Tech / LED')
    entertainment_band_musicians_dj=fields.Text(string='Band / Musicians / DJ')
    entertainment_dance=fields.Text(string='Dance')
    entertainment_ambient=fields.Text(string='Ambient')
    entertainment_cirque=fields.Text(string='Cirque')


    activities_team_building=fields.Text(string='Team Building')
    activities_cruise=fields.Boolean(string='Cruise')


    manpower_emcee=fields.Text(string='Emcee')
    manpower_hostesses=fields.Boolean(string='Hostesses')
    manpower_ushers=fields.Boolean(string='Ushers')
    manpower_models=fields.Boolean(string='Models')
    manpower_security=fields.Boolean(string='Security')
    manpower_event_staff=fields.Boolean(string='Event Staff')
    manpower_interpreter=fields.Boolean(string='Interpreter')
    manpower_labor=fields.Boolean(string='Labor')
    manpower_delivery=fields.Boolean(string='Delivery')


    def _selection_state(self):
        return   [('client_info','client_info'),
            ('_event_info','_event_info'),
            ('_dmc_requirements','_dmc_requirements'),
            ('_design_requirements','_design_requirements'),
            ('_registration_requirements','_registration_requirements'),
            ('_equipment_requirements','_equipment_requirements'),
            ('_photo_video_requirements','_photo_video_requirements'),
            ('_production_branding','_production_branding'),
            ('_photobooth','_photobooth'),
            ('_others_misc_requirements','_others_misc_requirements'),
            ('_entertainment','_entertainment'),
            ('_manpower','_manpower')]
    @api.model
    def _Selection_state1(self):
        return   [('client_info','client_info'),
            ('_event_info','_event_info'),
            ('_dmc_requirements','_dmc_requirements'),
            ('_design_requirements','_design_requirements'),
            ('_registration_requirements','_registration_requirements'),
            ('_equipment_requirements','_equipment_requirements'),
            ('_photo_video_requirements','_photo_video_requirements'),
            ('_production_branding','_production_branding'),
            ('_photobooth','_photobooth'),
            ('_others_misc_requirements','_others_misc_requirements'),
            ('_entertainment','_entertainment'),
            ('_manpower','_manpower')]
    
    def open_next(self):
        self.ensure_one()

        index = self.total_state.index(self.state)
        
        # print(index,self.state)
        # _logger = logging.getLogger(__name__)
        # _logger.error(index,self.state)
        if  index +1  <len(self.total_state)-1:
            self.state = self.total_state[index+1]
        else:
            self.state = "final"
        print("we moved on %s"%self.state)
        name = self.state.replace("_", " ").strip().capitalize()
        return self._reopen_self(name)
    
    def open_previous(self):
        self.ensure_one()
        index = self.total_state.index(self.state)
        print(index,self.state)
        # _logger = logging.getLogger(__name__)
        # _logger.error(index,self.state)
        if  index <1:
            self.state = self.total_state[0]
        else:
            self.state = self.total_state[index-1]
        name = self.state.replace("_", " ").strip().capitalize()
        return self._reopen_self(name)
    
    def convert_to_sale_order(self):
        pass

    def _reopen_self(self,name):
        
        
        return {
            "type": "ir.actions.act_window",
            "res_model": self._name,
            "res_id": self.id,
            "view_mode": "form",
            "target": "new",
            "name":name

        }


        