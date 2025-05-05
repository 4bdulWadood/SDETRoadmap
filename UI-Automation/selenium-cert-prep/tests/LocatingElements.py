from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

# Locate the search box using :
# ID, Name, XPath, CSS Selector, Link Text, Partial Link Text, Tag Name, Class Name
# The By method in Selenium is used to locate Class Names, ID, and XPath, etc.

# Element Finder Challenge
# Open https://www.saucedemo.com/ 
# Locate :
    # Username and Password Fields
    # Login Button
    # Error Message Area

username = driver.find_element(By.ID, "user-name")
password = driver.find_element(By.NAME, "password")

# send_keys() method is used to simulate typing into an input field or any editable input element on a web page
username.send_keys("standard_user")  
password.send_keys("secret_sauce")

login_button = driver.find_element(By.CLASS_NAME, "btn_action")
login_button.click()

driver.quit()

