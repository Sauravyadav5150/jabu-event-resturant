# import sys
# import os
 
# # getting the name of the directory
# # where the this file is present.
# current = os.path.dirname(os.path.realpath(__file__))
 
# # Getting the parent directory name
# # where the current directory is present.
# parent = os.path.dirname(current)
 
# # adding the parent directory to 
# # the sys.path.
# sys.path.append(parent)
 
# # now we can import the module in the parent
# # directory.
# import  base

# class wizardTest(base.base):
#     def setUp(self):
#         # Replace 'path_to_chromedriver' with the path to your ChromeDriver executable
#         self.driver = webdriver.Chrome(executable_path='path_to_chromedriver')
#         self.driver.implicitly_wait(10)  # Implicit wait to handle synchronization issues

#     def tearDown(self):
#         # Close the browser after each test
#         self.driver.quit()

#     def test_create_events_wizard(self):
#         # Open the Odoo website where the wizard is located
#         self.driver.get("http://localhost:8069/web/login")
        
#         # Log in to Odoo
#         username_input = self.driver.find_element(By.ID, "login")
#         password_input = self.driver.find_element(By.ID, "password")
#         login_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Log in')]")

#         username_input.send_keys("your_username")
#         password_input.send_keys("your_password")
#         login_button.click()

#         # Wait for the main page to load
#         WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "oe_topbar_name")))

#         # Navigate to the create.events wizard
#         self.driver.get("http://localhost:8069/web#model=create.events&view_type=form")

#         # Wait for the wizard to load
#         WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "client_name")))

#         # Fill in client information
#         client_name = self.driver.find_element(By.ID, "client_name")
#         client_name.send_keys("Test Client")
#         company = self.driver.find_element(By.ID, "company")
#         company.send_keys("Test Company")
#         company_address = self.driver.find_element(By.ID, "company_address")
#         company_address.send_keys("123 Main Street")
#         registration_tax_id = self.driver.find_element(By.ID, "registration_tax_id")
#         registration_tax_id.send_keys("1234567890")
#         email_address = self.driver.find_element(By.ID, "email_address")
#         email_address.send_keys("test@example.com")
#         mobile = self.driver.find_element(By.ID, "mobile")
#         mobile.send_keys("+1234567890")
#         line_whatsapp_insta_fb = self.driver.find_element(By.ID, "line_whatsapp_insta_fb")
#         line_whatsapp_insta_fb.send_keys("test_username")
#         website = self.driver.find_element(By.ID, "website")
#         website.send_keys("https://www.example.com")

#         # Click Next
#         next_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Next')]")
#         next_button.click()

#         # Wait for the next page to load
#         WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "event_info_type_of_event")))

#         # Fill in event information
#         event_info_type_of_event = self.driver.find_element(By.ID, "event_info_type_of_event")
#         event_info_type_of_event.send_keys("Corporate")
#         event_info_event_date_start1 = self.driver.find_element(By.ID, "event_info_event_date_start1")
#         event_info_event_date_start1.send_keys("2024-03-30")
#         event_info_event_date_end1 = self.driver.find_element(By.ID, "event_info_event_date_end1")
#         event_info_event_date_end1.send_keys("2024-03-31")
#         event_info_destination = self.driver.find_element(By.ID, "event_info_destination")
#         event_info_destination.send_keys("Destination")
#         event_info_event_venue_s_ = self.driver.find_element(By.ID, "event_info_event_venue_s_")
#         event_info_event_venue_s_.send_keys("Event Venue")
#         event_info_no_of_pax = self.driver.find_element(By.ID, "event_info_no_of_pax")
#         event_info_no_of_pax.send_keys("100")
#         event_info_events_s_details_event_info = self.driver.find_element(By.ID, "event_info_events_s_details_event_info")
#         event_info_events_s_details_event_info.send_keys("Event Details")
#         event_info_themes = self.driver.find_element(By.ID, "event_info_themes")
#         event_info_themes.send_keys("Event Themes")

#         # Click Next
#         next_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Next')]")
#         next_button.click()

#         # Wait for the next page to load
#         WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "dmc_requirements_airport_transfers")))

#         # Fill in DMC requirements
#         dmc_requirements_airport_transfers = self.driver.find_element(By.ID, "dmc_requirements_airport_transfers")
#         dmc_requirements_airport_transfers.click()
#         dmc_requirements_airport_rep_service = self.driver.find_element(By.ID, "dmc_requirements_airport_rep_service")
#         dmc_requirements_airport_rep_service.click()
#         dmc_requirements_ground_transportation = self.driver.find_element(By.ID, "dmc_requirements_ground_transportation")

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class TestEventWizard(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='C:\webdrivers')
        self.driver.implicitly_wait(10)  # Implicit wait for elements
        
    def test_event_wizard(self):
        # Test the Odoo event wizard functionality
        
        # Open the event wizard
        self.driver.get("http://localhost:8069/web/login")

        def runtest(self):
         self.login("test@dev.dev","saurav123")
        
        # Fill in client information
        self.driver.find_element_by_id("client_name").send_keys("John Doe")
        self.driver.find_element_by_id("company").send_keys("XYZ Corp")
        self.driver.find_element_by_id("company_address").send_keys("123 Main St")
        # Fill in more fields as needed
        
        # Click next to go to the next state
        self.driver.find_element_by_id("next_button").click()
        
        # Fill in event information
        self.driver.find_element_by_id("event_info_type_of_event").send_keys("Corporate")
        self.driver.find_element_by_id("event_info_event_date_start1").send_keys("2024-04-01")
        self.driver.find_element_by_id("event_info_event_date_end1").send_keys("2024-04-03")
        # Fill in more fields as needed
        
        # Click next to go to the next state
        self.driver.find_element_by_id("next_button").click()
        
        # Fill in DMC requirements
        self.driver.find_element_by_id("dmc_requirements_airport_transfers").click()
        self.driver.find_element_by_id("dmc_requirements_ground_transportation").click()
        # Fill in more fields as needed
        
        # Click next to go to the next state
        self.driver.find_element_by_id("next_button").click()
        
        # Fill in design requirements
        self.driver.find_element_by_id("design_requirements_artwork").click()
        self.driver.find_element_by_id("design_requirements_design").click()
        # Fill in more fields as needed
        
        # Click next to go to the next state
        self.driver.find_element_by_id("next_button").click()
        
        # Fill in registration requirements
        self.driver.find_element_by_id("registration_requirements_registration_counter").click()
        self.driver.find_element_by_id("registration_requirements_registration_staff").click()
        # Fill in more fields as needed
        
        # Click next to go to the next state
        self.driver.find_element_by_id("next_button").click()
        
        # Fill in equipment requirements
        self.driver.find_element_by_id("equipment_requirements_light_equipment").click()
        self.driver.find_element_by_id("equipment_requirements_sound_equipment").click()
        # Fill in more fields as needed
        
        # Click next to go to the next state
        self.driver.find_element_by_id("next_button").click()
        
        # Fill in photo/video requirements
        self.driver.find_element_by_id("photo_video_requirements_photo").click()
        self.driver.find_element_by_id("photo_video_requirements_video").click()
        # Fill in more fields as needed
        
        # Click next to go to the next state
        self.driver.find_element_by_id("next_button").click()
        
        # Fill in production/branding requirements
        self.driver.find_element_by_id("production_branding_standees").click()
        self.driver.find_element_by_id("production_branding_backdrops").click()
        # Fill in more fields as needed
        
        # Click next to go to the next state
        self.driver.find_element_by_id("next_button").click()
        
        # Fill in photobooth requirements
        self.driver.find_element_by_id("photobooth_standard_photobooth_backdrop_only").click()
        self.driver.find_element_by_id("photobooth_standard_photobooth_images_print").click()
        # Fill in more fields as needed
        
        # Click next to go to the next state
        self.driver.find_element_by_id("next_button").click()
        
        # Fill in miscellaneous requirements
        self.driver.find_element_by_id("others_misc_requirements_gifts").send_keys("Gifts for attendees")
        self.driver.find_element_by_id("others_misc_requirements_trophy_awards").click()
        # Fill in more fields as needed
        
        # Click next to go to the next state
        self.driver.find_element_by_id("next_button").click()
        
        # Fill in entertainment requirements
        self.driver.find_element_by_id("entertainment_thai_theme").send_keys("Thai traditional dancers")
        self.driver.find_element_by_id("entertainment_dance").send_keys("Dance performances")
        # Fill in more fields as needed
        
        # Click next to go to the next state
        self.driver.find_element_by_id("next_button").click()
        
        # Fill in manpower requirements
        self.driver.find_element_by_id("manpower_emcee").send_keys("Experienced emcee")
        self.driver.find_element_by_id("manpower_security").click()
        # Fill in more fields as needed
        
        # Click next to go to the final state
        self.driver.find_element_by_id("next_button").click()
        
      
        current_state = self.driver.find_element_by_xpath("//label[contains(text(),'State')]/following-sibling::div/span").text
        self.assertEqual(current_state, "Final", "Event wizard should be in the final state")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
