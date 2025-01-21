import smtplib, ssl
from mailersend import emails
import requests

mailinglist = ["syd@hanby.org.uk","sydney.hanby-howard.226@accesscreative.ac.uk","willow.moody.468@accesscreative.ac.uk"]

api_key = "HIDDEN LOCALLY FOR SECURITY"

mailer = emails.NewEmail(mailersend_api_key=api_key)


def Mailer():
    
    for i in range(len(mailinglist)):
        mail_body = {}

        mail_from = {
            "name": "GregBotNetwork",
            "email": "HIDDEN LOCALLY FOR SECURITY",
        }

        recipients = [
            {
                "name": "GregbotUser",
                "email": mailinglist[i],
            }
        ]

        mailer.set_mail_from(mail_from, mail_body)
        mailer.set_mail_to(recipients, mail_body)
        mailer.set_subject("Email testing for the GregBot!", mail_body)
        mailer.set_html_content("Thanks for being part of the email testing operation!!!", mail_body)
        mailer.set_plaintext_content("Thanks for being part of the email testing operation!!!", mail_body)

        print(mail_body)

        mailer.send(mail_body)
        
    
Mailer()