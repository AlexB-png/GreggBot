from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
import time
import keyboard

def access_website(email):
    driver = None
    try:
        driver = webdriver.Firefox() # Initialize a Firefox webdriver
        driver.get("https://launch.huggg.me/super/p7iPuMm9h4lRiM9")
        driver.find_element(By.CSS_SELECTOR, ".button-module_button__WDVlB.landing_moreInfoButton__eMFex").click()
        driver.find_element(By.CSS_SELECTOR, ".button-module_button__WDVlB").click()
        driver.find_element(By.ID, "email").send_keys(email)
        keyboard.press_and_release("enter")
        driver.find_element(By.CSS_SELECTOR, ".button-module_button__WDVlB.confirm_confirmButton__15iRE").click()
        driver.close()
    except NoSuchElementException as e:
        print(f"Error: Element not found. {e}")
    except TimeoutException as e:
        print(f"Error: The operation timed out. {e}")
    except WebDriverException as e:
        print(f"Error: WebDriver issue occurred. {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        # Ensure the driver is closed properly
        if driver:
            driver.close()

access_website("your_email@example.com")