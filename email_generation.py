# pip install mailslurp-client
import mailslurp_client
from faker import Faker
import bs4 as BeautifulSoup
import re

def CreateEmail(runtype):
    
    # create a mailslurp configuration
    mailslurp_configuration = mailslurp_client.Configuration()
    mailslurp_configuration.api_key['x-api-key'] = "f6300f98f869a831f9407f18df987a9a5ceb931e7926b500b44e28ec51b54691"
    
    with mailslurp_client.ApiClient(mailslurp_configuration) as api_client:
        
        fake = Faker()
        
        inbox_controller = mailslurp_client.InboxControllerApi(api_client)
        options = mailslurp_client.CreateInboxDto()
        options.name = fake.name()
        options.inbox_type = "SMTP_INBOX"
        inbox = inbox_controller.create_inbox_with_options(options)
        
        if runtype == "self":
            return inbox
        elif runtype == "mainL":
            return inbox.email_address
        


inbox = CreateEmail("self")

#email_ID = inbox.id


def ParseLink(email_address):
    
    # create a mailslurp configuration
    mailslurp_configuration = mailslurp_client.Configuration()
    mailslurp_configuration.api_key['x-api-key'] = "f6300f98f869a831f9407f18df987a9a5ceb931e7926b500b44e28ec51b54691"
    
    with mailslurp_client.ApiClient(mailslurp_configuration) as api_client:
        
        #Translates the email address recieved into an inbox id (slightly weird workaround but its not much overhead :shrug)
        inbox_controller = mailslurp_client.InboxControllerApi(api_client)
        inbox_by_email = inbox_controller.get_inbox_by_email_address(
        email_address
        )
        print(0)
        
        #Wait for email to be recieved
        wait_for_controller = mailslurp_client.WaitForControllerApi(api_client)
        print(1)
        email = wait_for_controller.wait_for_latest_email(
            inbox_id=inbox_by_email.id, timeout=60_000, unread_only=True
        )
        print(2)
        
        #Parse the link from huggg

        huggg_p_link = r"https://launch\.huggg\.me/([A-Za-z0-9]{16})"

        matches=re.findall(huggg_p_link, str(email))
        print(matches)
        
        huggg_link_concat = "https://launch.huggg.me/" + matches[0]
        print(huggg_link_concat)
        
        return huggg_link_concat