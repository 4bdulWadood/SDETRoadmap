

# Exercise 1 : Wait for Dynamic Element Load (Explicit Wait)
# Dynamic elements loading refers to those elements that are not immediately available or visible when the page loads but are 
# rendered later, typically due to :
# - JavaScript execution
# AJAX Calls
# User Interactions (like clicking a button to load more content)
# Use WebDriverWait and ExpectedConditions to handle Dynamic Content.


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

# Maximize window to avoid layout issues.
driver.maximize_window()

wait = WebDriverWait(driver, 10)
start_button = wait.until(EC.element_to_be_clickable((By.ID, "start")))

start_button.click()

#WebDriverWait is used to wait for a certain condition to occur before proceeding with the next step in the code.
wait = WebDriverWait(driver, 10) # waits up to 10 seconds for the condition to be met
element = wait.until(
    # EC.presence_of_element_located only ensures the element is in the DOM, not that it's visible (i.e., not hidden with display: none). EC.presence_of_element_located((By.ID, "finish"))
    EC.visibility_of_element_located((By.ID, "finish"))
)

finish_button = driver.find_element(By.ID, "finish")

try:
    finish_button = driver.find_element(By.ID, "finish")
    assert finish_button.text == "Hello World!", f"Expected 'Hello World!', but got '{finish_button.text}'"
except AssertionError as e:
    print(f"AssertionError: {e}")
except Exception as e:
    print(f"An error occurred: {e}")

# 1. WebDriverWait : Sets a maximum timeout for how long the script will wait for a condition to be met. This is like telling the
# script to wait for a specific amount of time before giving up. 

# 2. wait.until() : This is where you specify the condition you want to check. The script will repeatedly check this condition at intervals. (
# e.g.., every 500ms) until it's satisfied or the timeout is reached.

driver.quit()


