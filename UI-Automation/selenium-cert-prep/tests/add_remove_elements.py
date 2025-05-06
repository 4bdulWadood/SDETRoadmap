import time
from selenium.common.exceptions import StaleElementReferenceException
'''
Exercise 2: Handle StaleElementReferenceException on Dynamic List Update
Goal : Practice refreshing elements when the DOM changes.

Scenario:
Use https://the-internet.herokuapp.com/add_remove_elements/ to add and remove elements dynamically.

Task :
* Add 3 Buttons using "Add Element" button.
* Delete the first button, then try to click the second button.
* Intentionally catch and recover from StaleElementReferenceException.

Key Concepts:
* Handling Stale Elements.
* Re-locating elements before trying.
* Exception handling.

Stale Elements in Selenium are elements that were previously interactable but are no longer attached to the DOM (Document Object Model) when you try to access it again. 
This can happen if :
* The element was removed, updated, or re-rendered (e.g., due to dynamic page changes, like JS updates)
* The page was refreshed or navigated away from.

In short, stale elements are those that were valid at the time of retrieval, but by the time you try to interact with them, they
are no longer existing or are in an inconsistent state in the DOM.
'''

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

# Target the button within the .example container
add_button = driver.find_element(By.CSS_SELECTOR, ".example button")
add_button.click()
add_button.click()
add_button.click()

time.sleep(1)

# Locate the container div
elements_div = driver.find_element(By.ID, "elements")

# Get all buttons inside the #elements div
buttons = elements_div.find_elements(By.TAG_NAME, "button")

driver.execute_script("arguments[0].remove();", buttons[0])

'''
driver.execute_script("arguments[0].remove();", buttons[0])

    When you remove a DOM element (like the first button), using JS, the original 'buttons' list becomes stale, because it still
    holds references to elements that no longer exist in the DOM. 

    That's why you get this error.
    StaleElementReferenceException: Message: Stale element reference: element is not attached to the page document.

    Selenium elements are like 'live pointers' to specific nodes in the DOM.
    Once that node is removed, your pointer becomes invalid, and accessing it throws StaleElementReferenceException.
    Re-fetching gets fresh references from the current DOM.

'''

try:
    # Delete the first button
    driver.execute_script("arguments[0].remove();", buttons[0])
    print("First button deleted.")

    # Try clicking the second (which is now first)
    buttons[1].click()

except StaleElementReferenceException:
    print("StaleElementReferenceException caught — refreshing element list...")

    # Re-fetch the elements after DOM change
    buttons = driver.find_elements(By.CSS_SELECTOR, "#elements button")
    if buttons:
        buttons[0].click()
        print("Clicked the refreshed second button.")
    else:
        print("No buttons available after refresh.")

# Pause to observe result
time.sleep(3)

driver.quit()
