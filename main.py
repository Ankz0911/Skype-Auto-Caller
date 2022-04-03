from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from random import randint
import time as timer

# Constants
USERNAME = "your_email"
PASSWORD = "your_password"

# step- 0 initialising selenium
chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.delete_all_cookies()
driver.get("https://go.skype.com/myaccount")
driver.maximize_window()

# step - 1 click on 'Sign in'
timer.sleep(2)
input_element = driver.find_element_by_name("loginfmt")
input_element.send_keys(USERNAME)
timer.sleep(2)
button = driver.find_element_by_id("idSIButton9")
button.click()

# step - 2 enter password
input_element = driver.find_element_by_name("passwd")
input_element.send_keys(PASSWORD)
timer.sleep(2)
button = driver.find_element_by_id("idSIButton9")
button.click()

button = driver.find_element_by_id("idBtn_Back")
button.click()

# step 3 - navigate to skype web
driver.get("https://web.skype.com/")
timer.sleep(5)
element = driver.find_element_by_id("rx-vlv-2")
element.click()
timer.sleep(2)
button = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div[1]/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div[2]/div[2]/button')
button.click()
button = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div/button/div/div')
button.click()
timer.sleep(200)
driver.quit()
