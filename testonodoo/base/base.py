
from selenium import webdriver     
 
# For using sleep function because selenium 
# works only when the all the elements of the 
# page is loaded.
import time 
  
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By

 
# Creating an instance webdriver


#python
class base:
    browser = None 
    base_url = ""
    def __init__(self,base_url):
        browser = webdriver.Chrome() 
        self.browser = browser
        self.base_url = base_url
        pass
    def login(self,username,password):
        self.browser.get("%s/web/login"%self.base_url)
        time.sleep(2)
        element = self.browser.find_element(By.ID,"login")
        element.send_keys(username)
        time.sleep(2)
        element= self.browser.find_element(By.ID,"password")
        element.send_keys(password)
        time.sleep(2)
        LOG = self.browser.find_elements(By.XPATH, '//*[@type="submit"]')
        LOG[0].click()
        time.sleep(2)
        pass 

    def confirmRoles():

        pass
    def logout(self):
        pass
    def create_records(self,data):
        pass
    def move_menu(self,menu_name):
        pass
    def fill_field(self,fieldname,value):
        pass

    def runtest():
        pass

    def processRole(self):
        self.runtest()
        self.confirmRoles()

'''
C++ class
function are 
function login(){

}
class base{
function base(value1,value2){

}

function login(){

}

function ~base(){

}

}

y = base(value1,value2)
y.function()
delete y 
'''