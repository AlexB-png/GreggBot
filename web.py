from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.firefox.options import Options
import keyboard
from typing import Union
import helper


def access_website(email) -> Union[str, int]:
    driver = None
    error: str = ""
    try:
        options = Options()
        options.headless = True # Run the browser in headless mode
        driver = webdriver.Firefox() # Initialize a Firefox webdriver
        driver.get("https://launch.huggg.me/super/p7iPuMm9h4lRiM9")
        driver.find_element(By.CSS_SELECTOR, ".button-module_button__WDVlB.landing_moreInfoButton__eMFex").click()
        driver.find_element(By.CSS_SELECTOR, ".button-module_button__WDVlB").click()
        driver.find_element(By.ID, "email").send_keys(email)
        keyboard.press_and_release("enter")
        driver.find_element(By.CSS_SELECTOR, ".button-module_button__WDVlB.confirm_confirmButton__15iRE").click()
        driver.close()
    except NoSuchElementException as e:
        error: str = f"Element not found. {e}"
    except TimeoutException as e:
        error: str = f"Webpage timed out. {e}"
    except WebDriverException as e:
        error: str = f"A WebDriver error occurred. {e}"
    except Exception as e:
        error: str = f"An unexpected error occurred. {e}"
    finally:
        # Ensure the driver is closed properly
        if driver and error == "":  # If no error occurred, close the driver and return 0:
            driver.close()
            return 0
        else:
            if driver:
                driver.close()
            return error