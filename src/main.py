from typing import Union
import web
import helper
import json
import pathlib
from pathlib import Path

def main():
    current_dir = Path.cwd()
    parent_dir = current_dir.parent
    data_path = Path(parent_dir / "data")
    print("got path")
    if not data_path.exists():
        helper.setup() # Function to set up data folder goes here
        helper.setup_emails()

    path = Path(data_path / "emails.json")
    
    with open(path, "r") as f:
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
            result: Union[str, int] = web.access_website(email_new)
            if result != 0:
                if not helper.log_errors(result):
                    print("Failed to log error")
    with open(path, "w") as f:
        json.dump(data, f)
                    

    # Function to get link from email goes here

if __name__ == "__main__":
    main()
    