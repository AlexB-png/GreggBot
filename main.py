from typing import Union
import modules.web_tools as web_tools
import modules.helper as helper
import json
from pathlib import Path
import time
from web.inputs import app
import schedule
import threading

def main():
    current_dir = Path.cwd()
    data_path = Path(current_dir / "data")
    email_path = Path(current_dir / "web" / "static" / "emails.json")
    with open(email_path, "r") as f:

        data = json.load(f)
        print(data)
        for dict in data:
            email = data[dict]["email"]
            uses = data[dict]["uses"]
            temp = email.split("@")
            data[dict]["uses"] += 1
            temp[0] += f"+{uses+1}"
            email_new = "@".join(temp)
            result: Union[str, int] = web_tools.access_website(email_new)
            if result != 0:
                if not helper.log_errors(result):
                    print("Failed to log error")
                    
    with open(email_path, "w") as f:
        json.dump(data, f, indent=4)
                    

def run_tasks():
    while True:
        schedule.run_pending()
        time.sleep(1)

def start_flask():
    # Enables us to run the flask app in a separate thread
    app.run(host="0.0.0.0", port=5000)

def check_directories():
    current_dir = Path.cwd()
    data_path = Path(current_dir / "data")
    email_path = Path(current_dir / "web" / "static" / "emails.json")
    if not data_path.exists():
        helper.setup() # Function to set up data folder goes here
    if not email_path.exists():
        helper.setup_emails() # Function to set up email folder goes here

if __name__ == "__main__":
    check_directories()

    # Schedule tasks to run at specific times
    schedule.every().day.at("08:00").do(main)
    schedule.every().day.at("11:30").do(main)
    schedule.every().day.at("16:00").do(main)

    # Start Flask in a separate thread so the scheduler can run
    flask_thread = threading.Thread(target=start_flask, daemon=True)
    flask_thread.start()

    # Run the scheduler
    run_tasks()
