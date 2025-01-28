from typing import Union
import src.web_tools as web_tools
import src.helper as helper
import json
import pathlib
from pathlib import Path
import datetime
import time
from web.inputs import app

def main():
    current_dir = Path.cwd()
    data_path = Path(current_dir / "data")
    email_path = Path(current_dir / "web" / "static" / "emails.json")
    with open(email_path, "r") as f:

        data = json.load(f)
        print(data)
        for dict in data:
            print("Should get email")
            email = data[dict]["email"]
            uses = data[dict]["uses"]
            temp = email.split("@")
            data[dict]["uses"] += 1
            temp[0] += f"+{uses+1}"
            email_new = "@".join(temp)
            print(email_new)
            
            result: Union[str, int] = web_tools.access_website(email_new)
            if result != 0:
                if not helper.log_errors(result):
                    print("Failed to log error")
                    
    with open(email_path, "w") as f:
        json.dump(data, f, indent=4)
                    

    # Function to get link from email goes here

if __name__ == "__main__":
    current_dir = Path.cwd()
    data_path = Path(current_dir / "data")
    email_path = Path(current_dir / "web" / "static" / "emails.json")
    if not data_path.exists():
        helper.setup() # Function to set up data folder goes here
    if not email_path.exists():
        helper.setup_emails() # Function to set up email folder goes here
    while True:
        app.run()
        time.sleep(60)
        main()