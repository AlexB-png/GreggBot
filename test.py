import smtplib, ssl
import requests

#Only using this currently
from mailersend import emails


#Placeholder data before the mailing list DB is created
mailing_list = ["syd@hanby.org.uk","sydney.hanby-howard.226@accesscreative.ac.uk","willow.moody.468@accesscreative.ac.uk"]

#The API key for verifing to Mailer Send that its us
api_key = "HIDDEN LOCALLY FOR SECURITY"

#Creates a new mailer and takes in the API KEY
mailer = emails.NewEmail(mailersend_api_key=api_key)


def Mailer():
    
    #Loops through all people signed up for the mailing list
    for i in range(len(mailing_list)):
        
        #Email Body stuff
        mail_body = {}

        mail_from = {
            "name": "GregBotNetwork",
            #The Email adress user associated with the API key on Mailer Send
            "email": "HIDDEN LOCALLY FOR SECURITY",
        }

        recipients = [
            {
                "name": "GregbotUser",
                "email": mailing_list[i],
            }
        ]

        #Sets values for the mailer
        mailer.set_mail_from(mail_from, mail_body)
        mailer.set_mail_to(recipients, mail_body)
        mailer.set_subject("Email testing for the GregBot!", mail_body)
        mailer.set_html_content("Thanks for being part of the email testing operation!!!", mail_body)
        mailer.set_plaintext_content("Thanks for being part of the email testing operation!!!", mail_body)

        #For debugging
        print(mail_body)

        
        #Sends out the email
        mailer.send(mail_body)
        

#Runs the main code block
Mailer()