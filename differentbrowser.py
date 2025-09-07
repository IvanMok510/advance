import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

def run_chrome_test(url):
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    try:
        driver.get(url)
        print(f"Chrome: Page title is '{driver.title}'")
        driver.save_screenshot('chrome_screenshot.png')
    finally:
        driver.quit()

def run_firefox_test(url):
    service = FirefoxService(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    try:
        driver.get(url)
        print(f"Firefox: Page title is '{driver.title}'")
        driver.save_screenshot('firefox_screenshot.png')
    finally:
        driver.quit()

# Run tests sequentially
url = "https://www.google.com"
run_chrome_test(url)
run_firefox_test(url)
