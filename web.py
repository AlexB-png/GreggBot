from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def access_website():
    driver = webdriver.Firefox() # Initialize a Firefox webdriver
    driver.get("https://launch.huggg.me/super/p7iPuMm9h4lRiM9")
    html = driver.page_source
    print(html)
    browser.close()

access_website()