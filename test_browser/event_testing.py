

import time
import json
from selenium.webdriver.support.ui import WebDriverWait  
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestFailVaruntest():
  def setup_method(self):
    self.driver = webdriver.Chrome()
    self.vars = {}
    driver = self.driver
    # get google.co.in 
    driver.get("http://localhost:8069/web/login") 
    driver.find_element(By.ID, "login").send_keys("test@dev.dev")
    driver.find_element(By.ID, "password").send_keys("saurav123")
    #driver.get("http://localhost:8069/web/login")
    driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    try: 
      # wait 10 seconds before looking for element 
      element = WebDriverWait(driver, 10).until( 
        expected_conditions.presence_of_element_located((By.CLASS_NAME, "o_navbar")) 
      ) 
      get_url= driver.current_url
    finally: 
      # else quit 
      get_url= driver.current_url
    time.sleep(3)
  def teardown_method(self, method):
    self.driver.quit()

  def test_failVaruntest(self):
    self.driver.get("http://localhost:8069/web")
    self.driver.set_window_size(1140, 538)
    self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    driver = self.driver
    try: 
      # wait 10 seconds before looking for element 
      element = WebDriverWait(driver, 10).until( 
        expected_conditions.presence_of_element_located((By.ID, "name")) 
      ) 
      get_url= driver.current_url
    finally: 
      # else quit 
      get_url= driver.current_url

    self.driver.find_element(By.ID, "name").send_keys("Varun")
    self.driver.find_element(By.ID, "event_name").send_keys("Var")
    self.driver.find_element(By.ID, "event_type").send_keys("Var")
    self.driver.find_element(By.ID, "event_date").click()
    self.driver.find_element(By.ID, "venues_id").send_keys("1")
    self.driver.find_element(By.ID, "themes_id").send_keys("12123")
    # self.driver.find_element(By.CSS_SELECTOR, ".o_content").click()
    # self.driver.find_element(By.CSS_SELECTOR, ".active").click()
    time.sleep(3)
    #element = 
    self.driver.find_element(By.CSS_SELECTOR, ".o_form_button_save").click()
    # actions = ActionChains(self.driver)
    # actions.move_to_element(element).perform()
    # element = self.driver.find_element(By.CSS_SELECTOR, "body")
    # actions = ActionChains(self.driver)
    #actions.move_to_element(element, 0, 0).perform()
    # self.driver.find_element(By.CSS_SELECTOR, ".fa-cloud-upload").click() 
    time.sleep(3)
    self.driver.find_element(By.CSS_SELECTOR, ".o_back_button > a").click()
    time.sleep(3)
    assert self.driver.title == "Odoo - Member Window"

y = TestFailVaruntest()
y.setup_method()
y.test_failVaruntest()



# try:
#     1/1
# except:
#     print("this is an infinity")
# finally:
#     print("this will always run")