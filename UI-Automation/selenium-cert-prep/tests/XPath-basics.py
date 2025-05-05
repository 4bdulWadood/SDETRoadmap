from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.google.com/")

# Goal : Use WebDriver methods to interact with webpage elements.
# Topics :
# Click()
# send_keys()
# clear()
#text or .get_attribute("value")

search_bar = driver.find_element(By.ID, "APjFqb")

# send_keys() method is used to simulate typing into an input field or any editable input element on a web page
search_bar.send_keys("Syed Abdul Wadood")  
search_bar.send_keys(Keys.RETURN)  # Simulate pressing the Enter key

# Explicit wait : Wait until the search results container is visible.
try:
    results = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "rso"))
    )
    print("Search results loaded!")
except:
    print("Search results did not load in time.")

search_results = driver.find_element(By.CLASS_NAME, "dURPMd")
first_child = search_results.find_element(By.XPATH, "./*")
h3_element = first_child.find_element(By.XPATH, ".//h3")

print("First search result title:", h3_element.text)

driver.quit()
