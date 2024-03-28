
import base 
from selenium import webdriver     
 
# For using sleep function because selenium 
# works only when the all the elements of the 
# page is loaded.
import time 
  
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
 
# Creating an instance webdriver
# browser = webdriver.Chrome() 

class test_sales_guy(base.base):
    #method overriding 
    def __init__(self,base_url):
        # self.browser = browser
        self.base_url = base_url
        super().__init__(base_url)
        pass
        
    def login(self,username,password):
        super().login(username,password)
        pass
    def runtest(self):
        self.login("sale_manager@test.dev","test")

    def confirmRoles(self):
        menuItems = self.browser.find_elements(By.CLASS_NAME,".o-dropdown--menu.dropdown-menu.d-block")
        for item in menuItems:
            if item.text == "Settings":
                assert(False)
        time.sleep(2)
    


# z = test_sales_guy(browser,"http://localhost:8069/")

# z.runtest()