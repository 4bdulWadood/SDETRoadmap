from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import time

# Setup WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 15)
driver.maximize_window()

# 1. Open dropdown
dropdown = driver.find_element(By.CSS_SELECTOR, ".select2-container")
dropdown.click()

# 2. Type in search (triggers AJAX)
search_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".select2-search__field"))
)
search_input.send_keys("test")

# 3. Wait for AJAX results to load
results = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".select2-results__option"))
)

# 4. Select first result
if results:
    results[0].click()
