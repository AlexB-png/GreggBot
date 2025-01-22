import pyperclip
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException
import time
import keyboard


def open_10minutemail():
    # Set Chrome options to suppress unnecessary logs
    chrome_options = Options()
    chrome_options.add_argument("--disable-logging")  # Disable logging
    chrome_options.add_argument("--log-level=3")  # Suppress all but errors
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Initialize the driver with Chrome options
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://10minutemail.com/")

    # Wait for and close the consent popup if it appears
    try:
        consent_button = WebDriverWait(driver, 30).until(  # Increased timeout here
            EC.element_to_be_clickable((By.CSS_SELECTOR, "p.fc-button-label"))
        )
        consent_button.click()  # Close the consent popup
        print("Consent popup closed.")
    except Exception as e:
        print("No consent popup or error in closing:", e)

    # Wait for the email address element to be visible
    wait = WebDriverWait(driver, 30)  # Increased timeout here
    email_element = wait.until(
        EC.visibility_of_element_located((By.ID, "copy_address"))
    )

    # Ensure any overlay is removed or hidden
    try:
        overlay = driver.find_element(By.CSS_SELECTOR, ".fc-dialog-overlay")
        driver.execute_script("arguments[0].style.display = 'none';", overlay)
        print("Overlay hidden.")
    except Exception as e:
        print("No overlay found or error in hiding:", e)

    # Wait for the overlay to disappear (if it is still present)
    try:
        WebDriverWait(driver, 30).until(  # Increased timeout here
            EC.invisibility_of_element_located((By.CSS_SELECTOR, ".fc-dialog-overlay"))
        )
        print("Overlay is invisible.")
    except Exception as e:
        print("Error waiting for overlay to disappear:", e)

    # Try to extract the email address from the 'data-clipboard-text' attribute
    email_address = email_element.get_attribute('data-clipboard-text')

    if not email_address:
        # If no email address in 'data-clipboard-text', click the element to copy to clipboard
        try:
            # Use JavaScript to click if Selenium's normal click isn't working
            driver.execute_script("arguments[0].click();", email_element)
            print("Click triggered via JavaScript.")
        except Exception as e:
            print("Error clicking the email element:", e)

        # Wait a moment for the clipboard action to complete
        time.sleep(1)

        # Retrieve the copied email address from the clipboard
        email_address = pyperclip.paste()

    # Print the extracted email address
    if email_address:
        print("Email Address:", email_address)
    else:
        print("Email address could not be extracted.")

    return driver, email_address


def access_website(email, driver):
    try:
        # Open a new tab to interact with the website
        driver.execute_script("window.open('');")
        
        # Switch to the new tab (index 1 for the new tab)
        driver.switch_to.window(driver.window_handles[1])

        # Now navigate to the target website
        driver.get("https://launch.huggg.me/super/p7iPuMm9h4lRiM9")

        # Wait for and click on the first button
        button1 = WebDriverWait(driver, 30).until(  # Increased timeout here
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".button-module_button__WDVlB.landing_moreInfoButton__eMFex"))
        )
        button1.click()
        print("First button clicked.")

        # Wait for and click on the second button
        button2 = WebDriverWait(driver, 30).until(  # Increased timeout here
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".button-module_button__WDVlB"))
        )
        button2.click()
        print("Second button clicked.")

        # Wait for the email input and type the email address
        email_input = WebDriverWait(driver, 30).until(  # Increased timeout here
            EC.element_to_be_clickable((By.ID, "email"))
        )
        email_input.send_keys(email)

        # Press the "Enter" key using the keyboard module
        keyboard.press_and_release("enter")

        # Wait for the "CONFIRM EMAIL" button to become clickable and then click it
        confirm_email_button = WebDriverWait(driver, 30).until(  # Increased timeout here
            EC.element_to_be_clickable((By.XPATH, "//div[text()=\"CONFIRM EMAIL\"]"))
        )
        confirm_email_button.click()
        print("CONFIRM EMAIL button clicked.")

        # Wait for the "YUP THAT'S THE ONE!" button to become clickable and then click it
        yup_button = WebDriverWait(driver, 30).until(  # Increased timeout here
            EC.element_to_be_clickable((By.XPATH, "//div[text()=\"YUP THAT'S THE ONE!\"]"))
        )
        yup_button.click()
        print("YUP THAT'S THE ONE! button clicked.")

        # Confirm action and submit
        driver.find_element(By.CSS_SELECTOR, ".button-module_button__WDVlB.confirm_confirmButton__15iRE").click()
    except NoSuchElementException as e:
        print(f"Error: Element not found. {e}")
    except TimeoutException as e:
        print(f"Error: The operation timed out. {e}")
    except WebDriverException as e:
        print(f"Error: WebDriver issue occurred. {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Get the email address and the driver without closing the 10minutemail window
driver, TheEmailAddress = open_10minutemail()

# Now call access_website with the extracted email address and the driver
access_website(TheEmailAddress, driver)

# Both websites remain open, and no windows are closed automatically.
# The driver.quit() or driver.close() is not called automatically.
