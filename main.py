from typing import Union
import web
import email_tools
import helper

def main():
    helper.setup() # Function to set up data folder goes here

    # Imported function to generate email goes here

    email = "test@gmail.co" # Boilerplate to avoid param error
    result: Union[str, int] = web.access_website(email)
    if result != 0:
        if not helper.log_errors(result):
            print("Failed to log error")

    # Function to get link from email goes here

    result: Union[str, int] = email_tools.Mailer()
    if result != 0:
        if not helper.log_errors(result):
            print("Failed to log error")

if __name__ == "__main__":
    try:
        main()
    except ModuleNotFoundError as e:
        helper.log_errors(f"Module not found error: {e}")
    except TypeError as e:
        helper.log_errors(f"Type error: {e}")
    except ValueError as e:
        helper.log_errors(f"Value error: {e}")
    except Exception as e:
        helper.log_errors(f"An unexpected error occurred: {e}")