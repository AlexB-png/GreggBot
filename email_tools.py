import smtplib
import ssl
import requests
from mailersend import emails
from typing import Union

# Placeholder data before the mailing list DB is created
mailing_list = [
    "syd@hanby.org.uk",
    "sydney.hanby-howard.226@accesscreative.ac.uk",
    "willow.moody.468@accesscreative.ac.uk",
]

# The API key for verifying to MailerSend that it's us
api_key = "HIDDEN LOCALLY FOR SECURITY"

# Creates a new mailer and takes in the API key
mailer = emails.NewEmail(mailersend_api_key=api_key)

def Mailer() -> Union[int, str]:
    error: str = ""

    for i, recipient_email in enumerate(mailing_list):
        try:
            mail_body = {}
            mail_from = {
                "name": "GregBotNetwork",
                "email": "HIDDEN LOCALLY FOR SECURITY",
            }
            recipients = [
                {
                    "name": "GregbotUser",
                    "email": recipient_email,
                }
            ]

            mailer.set_mail_from(mail_from, mail_body)
            mailer.set_mail_to(recipients, mail_body)
            mailer.set_subject("Email testing for the GregBot!", mail_body)
            mailer.set_html_content(
                "Thanks for being part of the email testing operation!!!", mail_body
            )
            mailer.set_plaintext_content(
                "Thanks for being part of the email testing operation!!!", mail_body
            )

            mailer.send(mail_body)

        except emails.MailersendAPIError as api_error:
            error = f"MailerSend API error for {recipient_email}: {api_error}"
            break
        except smtplib.SMTPException as smtp_error:
            error = f"SMTP error for {recipient_email}: {smtp_error}"
            break
        except requests.exceptions.RequestException as network_error:
            error = f"Network error for {recipient_email}: {network_error}"
            break
        except Exception as e:
            error = f"An unexpected error occurred for {recipient_email}: {e}"
            break

    # Return 0 if no error, otherwise return the error message
    return 0 if error == "" else error

Mailer()