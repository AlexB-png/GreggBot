from typing import Union
import modules.web_tools as web_tools
import modules.helper as helper
import json
from pathlib import Path
import time
from web.inputs import app
import schedule
import threading
import datetime


def main():
    print("Main task started")
    current_dir = Path(__file__).parent  # Get the current script's directory
    data_path = Path(current_dir / "data")
    email_path = Path(current_dir / "web" / "static" / "emails.json")

    try:
        with open(email_path, "r") as f:
            data = json.load(f)
            print("Loaded email data")

            for dict in data:
                email = data[dict]["email"]
                uses = data[dict]["uses"]
                temp = email.split("@")
                data[dict]["uses"] += 1
                temp[0] += f"+{uses + 1}"
                email_new = "@".join(temp)
                result: Union[str, int] = web_tools.access_website(email_new)
                if result != 0:
                    if not helper.log_errors(f"Failed to access website with email {email_new}: {result}"):
                        print(f"Failed to log error for {email_new}")

        with open(email_path, "w") as f:
            json.dump(data, f, indent=4)
        print("Data saved successfully")

    except json.JSONDecodeError as e:
        error_message = f"Error decoding JSON file: {e}"
        print(error_message)
        helper.log_errors(error_message)
    except Exception as e:
        error_message = f"Unexpected error occurred: {e}"
        print(error_message)
        helper.log_errors(error_message)


def run_tasks():
    while True:
        schedule.run_pending()
        time.sleep(1)


def start_flask():
    # Ensures Flask runs only if not running in Gunicorn
    if not app.debug:
        app.run(host="0.0.0.0", port=5000)


def check_directories():
    current_dir = Path(__file__).parent
    data_path = Path(current_dir / "data")
    email_path = Path(current_dir / "web" / "static" / "emails.json")

    if not data_path.exists():
        helper.setup()  # Ensure setup() handles directory creation
    if not email_path.exists():
        helper.setup_emails()  # Ensure setup_emails() creates necessary files


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
