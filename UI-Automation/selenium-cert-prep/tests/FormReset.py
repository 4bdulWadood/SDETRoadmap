from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/automation-practice-form")

# Features : You can test :
# First Name, Last Name, Email Fields
# Gender Selection (Radio Buttons)
# Date Picker
# File Upload
# clear() and send_keys() on input fields

# Maximize window to avoid layout issues.
driver.maximize_window()

# Fill First Name
first_name = driver.find_element(By.ID, "firstName")
first_name.send_keys("Alice")

#Fill Last Name
last_name = driver.find_element(By.ID, "lastName")
last_name.send_keys("Smith")

# Fill Email
email = driver.find_element(By.ID, "userEmail")
email.send_keys("alice.smith@example.com")

# Wait for demo purposes
time.sleep(3)

email.clear()
last_name.clear()
first_name.clear()

time.sleep(3)

driver.quit()
