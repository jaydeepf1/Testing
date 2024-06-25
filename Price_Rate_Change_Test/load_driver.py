import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from logger import set_log
from find_free_port import find_free_port

# Initialize the custom logger
logger = set_log()

def load_options():
    """
    Configure Chrome options for WebDriver.
    """
    options = Options()
    options.add_argument("--log-level=3")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-software-rasterizer")
    options.add_argument("--disable-extensions")
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.9999.999 Safari/537.36 Edg/99.0.9999.999")
    # options.add_argument("--headless=new")  # Uncomment this line if running headless

    return options

def load_options_windows_chrome():
    """
    Configure Chrome options for Windows 11 with Chrome.
    """
    options = Options()
    options.add_argument("--log-level=3")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-software-rasterizer")
    options.add_argument("--disable-extensions")
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.9999.999 Safari/537.36")
    # Set geolocation to Atlanta, Georgia
    options.add_experimental_option('prefs', {
        'profile.default_content_setting_values': {
            'geolocation': 1
        },
        'profile.managed_default_content_settings': {
            'geolocation': 1
        },
        'profile.default_content_settings': {
            'geolocation': 1
        },
        'geolocation': {
            'latitude': 33.7490,
            'longitude': -84.3880
        }
    })
    return options

def load_options_ios_safari():
    """
    Configure Safari options for Apple iOS with Safari.
    """
    options = Options()
    options.add_argument("--log-level=3")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-software-rasterizer")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--allow-insecure-localhost")
    options.add_argument("--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1")
    # Set geolocation to Atlanta, Georgia
    options.add_experimental_option('prefs', {
        'profile.default_content_setting_values': {
            'geolocation': 1
        },
        'profile.managed_default_content_settings': {
            'geolocation': 1
        },
        'profile.default_content_settings': {
            'geolocation': 1
        },
        'geolocation': {
            'latitude': 33.7490,
            'longitude': -84.3880
        }
    })
    return options
    
def initialize_driver():
    """
    Initialize Chrome WebDriver with configured options and service.
    """
    options = load_options()
    # options = load_options_windows_chrome()
    # options = load_options_ios_safari()
    
    retry_count = 5

    for attempt in range(1, retry_count + 1):
        try:
            service = Service(port=find_free_port())
            driver = webdriver.Chrome(service=service, options=options)
            driver.maximize_window()
            driver.get('https://www.ihg.com/hotels/us/en/reservation')
            return driver  # If successful, return the driver
        except Exception as e:
            logger.error(f"Error initializing Chrome WebDriver (attempt {attempt}): {e}")
            if attempt == retry_count:
                logger.error("Failed to initialize Chrome WebDriver after multiple attempts.")
                raise SystemExit(1)
            time.sleep(5)  # Wait before retrying

def load_driver():
    driver = initialize_driver()
    return driver
