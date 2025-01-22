from typing import Union
import email_tools
import web
import helper

def main():
    helper.setup() # Function to set up data folder goes here

    # Imported function to generate email goes here

    email: None = None # Boilerplate to avoid param error
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
    main()