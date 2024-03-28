import base 

# For using sleep function because selenium 
# works only when the all the elements of the 
# page is loaded.
import time 

from selenium.webdriver.common.by import By
  

class tester(base.base):
    # def __init__(self,base_url):
    #     self.base_url = base_url
    #     pass
        
    def runtest(self):
        self.login("test@test.dev","test123")

    def confirmRoles(self):
        menuItems = self.browser.find_elements(By.CLASS_NAME,".o-dropdown--menu.dropdown-menu.d-block")
        for item in menuItems:
            if item.text == "Settings":
                assert(True)
        time.sleep(2)
        
        
        pass
