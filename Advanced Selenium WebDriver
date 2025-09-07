from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Set up ChromeDriver with Service
service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://the-internet.herokuapp.com/dropdown")

# Explicit Wait: Wait up to 10 seconds for dropdown to be clickable
wait = WebDriverWait(driver, 10)
dropdown = wait.until(EC.element_to_be_clickable((By.ID, "dropdown")))

# Select an option (using Select class for dropdowns)
from selenium.webdriver.support.ui import Select
select = Select(dropdown)
select.select_by_visible_text("Option 1")

# For hover example, navigate to hovers page
driver.get("https://the-internet.herokuapp.com/hovers")

# ActionChains: Hover over the first image
actions = ActionChains(driver)
image = driver.find_element(By.CSS_SELECTOR, ".figure:nth-child(3) img")  # First image
actions.move_to_element(image).perform()

# Verify user name appears on hover
user_name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".figure:nth-child(3) .figcaption h5")))
print("Hovered user:", user_name.text)  # Should print "name: user1"

# Execute JavaScript: Scroll to bottom
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Take screenshot (example)
driver.save_screenshot("hover_screenshot.png")

driver.quit()
