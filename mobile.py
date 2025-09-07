from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

def run_mobile_emulation_test(url, device_name='iPhone X'):
    """
    Emulate a mobile or tablet device in Chrome.
    :param url: The URL to test.
    :param device_name: Preset device name (e.g., 'iPhone X', 'iPad').
    """
    options = Options()
    mobile_emulation = {
        "deviceName": device_name  # Options: 'iPhone X', 'Pixel 2', 'Galaxy S5', 'iPad', etc.
    }
    options.add_experimental_option("mobileEmulation", mobile_emulation)
    
    # Initialize ChromeDriver using webdriver-manager
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    try:
        driver.get(url)
        print(f"Chrome Mobile ({device_name}): Page title is '{driver.title}'")
        driver.save_screenshot(f'chrome_{device_name.replace(" ", "_")}_screenshot.png')
        time.sleep(2)  # Pause to observe or add interactions
    finally:
        driver.quit()

# Run the test
if __name__ == "__main__":
    test_url = "https://www.google.com"
    run_mobile_emulation_test(test_url, "iPhone X")
