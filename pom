# This is a full, runnable example of the Page Object Model (POM) in Python for Advanced Selenium WebDriver.
# We'll use https://the-internet.herokuapp.com/ as the test site.
# This script includes:
# - Multiple POM classes (LoginPage and SecurePage).
# - Advanced features: Explicit waits, ActionChains (for hover if needed), JavaScript execution, and screenshot capture.
# - A main test function to demonstrate usage.
# - Error handling for login failure.

# Install dependencies if needed: pip install selenium webdriver-manager

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# POM Class for Login Page
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_locator = (By.ID, "username")
        self.password_locator = (By.ID, "password")
        self.submit_locator = (By.CSS_SELECTOR, "button[type='submit']")
        self.error_message_locator = (By.ID, "flash")

    def navigate_to(self):
        self.driver.get("https://the-internet.herokuapp.com/login")

    def enter_username(self, username):
        wait = WebDriverWait(self.driver, 10)
        username_field = wait.until(EC.presence_of_element_located(self.username_locator))
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.driver.find_element(*self.password_locator)
        password_field.send_keys(password)

    def click_submit(self):
        self.driver.find_element(*self.submit_locator).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_submit()

    def get_error_message(self):
        wait = WebDriverWait(self.driver, 10)
        error = wait.until(EC.visibility_of_element_located(self.error_message_locator))
        return error.text.strip()

# POM Class for Secure Page (after successful login)
class SecurePage:
    def __init__(self, driver):
        self.driver = driver
        self.logout_locator = (By.CSS_SELECTOR, "a.button")
        self.success_message_locator = (By.ID, "flash")

    def get_success_message(self):
        wait = WebDriverWait(self.driver, 10)
        success = wait.until(EC.visibility_of_element_located(self.success_message_locator))
        return success.text.strip()

    def click_logout(self):
        actions = ActionChains(self.driver)
        logout_button = self.driver.find_element(*self.logout_locator)
        actions.move_to_element(logout_button).perform()  # Hover example
        logout_button.click()

# Main test function demonstrating POM usage with advanced features
def run_pom_test():
    # Set up ChromeDriver with Service
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    try:
        # Initialize POM pages
        login_page = LoginPage(driver)
        secure_page = SecurePage(driver)
        
        # Navigate and perform login (successful case)
        login_page.navigate_to()
        login_page.login("tomsmith", "SuperSecretPassword!")
        
        # Verify success with explicit wait
        success_msg = secure_page.get_success_message()
        print("Success Message:", success_msg)  # Expected: "You logged into a secure area!"
        
        # Execute JavaScript: Scroll to bottom of the page
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        # Take screenshot after login
        driver.save_screenshot("secure_page_screenshot.png")
        print("Screenshot saved as 'secure_page_screenshot.png'")
        
        # Logout using ActionChains for hover
        secure_page.click_logout()
        
        # Verify back to login page
        wait = WebDriverWait(driver, 10)
        wait.until(EC.url_contains("/login"))
        print("Logged out successfully.")
        
        # Test failure case: Invalid login
        login_page.login("invalid", "wrongpass")
        error_msg = login_page.get_error_message()
        print("Error Message:", error_msg)  # Expected: "Your username is invalid!" or similar
        
        # Take screenshot on failure
        driver.save_screenshot("error_screenshot.png")
        print("Error screenshot saved as 'error_screenshot.png'")
    
    except Exception as e:
        print("Test failed:", str(e))
        driver.save_screenshot("failure_screenshot.png")
    
    finally:
        driver.quit()

# Run the test
if __name__ == "__main__":
    run_pom_test()
