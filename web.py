from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import keyboard

def access_website(email):
    driver = webdriver.Firefox() # Initialize a Firefox webdriver
    driver.get("https://launch.huggg.me/super/p7iPuMm9h4lRiM9")
    driver.find_element(By.CSS_SELECTOR, ".button-module_button__WDVlB.landing_moreInfoButton__eMFex").click()
    driver.find_element(By.CSS_SELECTOR, ".button-module_button__WDVlB").click()
    driver.find_element(By.ID, "email").send_keys(email)
    keyboard.press_and_release("enter")
    driver.find_element(By.CSS_SELECTOR, ".button-module_button__WDVlB.confirm_confirmButton__15iRE").click()
    driver.close() 