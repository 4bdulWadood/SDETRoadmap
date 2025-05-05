from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

# Goal : Use WebDriver methods to interact with webpage elements.
# Topics :
# Click()
# send_keys()
# clear()
#text or .get_attribute("value")

username = driver.find_element(By.ID, "user-name")
password = driver.find_element(By.NAME, "password")

# send_keys() method is used to simulate typing into an input field or any editable input element on a web page
username.send_keys("standard_user")  
password.send_keys("secret_sace")

login_button = driver.find_element(By.CLASS_NAME, "btn_action")
login_button.click()

try:
    # Check if the page title is "Products"
    assert driver.find_element(By.CLASS_NAME, "title").text == "Products"
    print("Login successful")
except AssertionError:
    print("Login failed: Title does not match expected value.")
except Exception as e:
    print(f"Login failed due to unexpected error: {e}")


driver.quit()



