# Python program to demonstrate 
# selenium 

# import webdriver 
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
# create webdriver object 
driver = webdriver.Chrome() 

# get google.co.in 
driver.get("http://localhost:8069/web/login") 
driver.find_element(By.ID, "login").send_keys("test@test.dev")
driver.find_element(By.ID, "password").send_keys("saurav123")
#driver.get("http://localhost:8069/web/login")
driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()


try: 
    # wait 10 seconds before looking for element 
    element = WebDriverWait(driver, 10).until( 
        EC.presence_of_element_located((By.CLASS_NAME, "o_navbar")) 
    ) 
    get_url= driver.current_url
finally: 
    # else quit 
    get_url= driver.current_url
    driver.quit() 


print(get_url)