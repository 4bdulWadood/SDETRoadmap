import time
from selenium.common.exceptions import StaleElementReferenceException
from selenium import webdriver
from selenium.webdriver.common.by import By

'''
Exercise 2: Browser Navigation Challenge (Back/Forward/Refresh)
Goal : Automate a multi-page scenario and use browser navigation controls.

Scenario:
Use https://www.selenium.dev/, Click on Downloads, then Projects.

Task :
* Navigate to Downloads Page
* Navigate to Projects Page.
* Use .back() and .forward() to return and validate page titles.
* Refresh the final page and assert content is still loaded.

Key Concepts:
* driver.back(), driver.forward(), driver.refresh()
* Page title and content assertion.
'''

driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/")

element = driver.find_element(By.XPATH, "//span[text()='Downloads']")
element.click()

element = driver.find_element(By.XPATH, "//span[text()='Projects']")
element.click()

time.sleep(5)

driver.back()

time.sleep(2)

driver.forward()

time.sleep(5)

driver.refresh()


driver.quit()



