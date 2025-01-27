import pathlib
import datetime
import json
from json import JSONDecodeError
import os


def log_errors(error_message):
    try:
        log_file_path = pathlib.Path("../data") / "error_log.json"
        if log_file_path.exists():
            with open(log_file_path, 'r') as file:
                error_logs = json.load(file)
        else:
            error_logs = []
        data = {
            'timestamp': str(datetime.datetime.now()),
            'error_message': error_message
        }
        error_logs.append(data)
        with open(log_file_path, 'w') as file:
            json.dump(error_logs, file, indent=4)

        return True
    except JSONDecodeError as e:
        print(f"Error decoding JSON file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred while logging errors: {e}")
    return False


def setup():
    try:
        folder_name = 'data'
        folder_path = os.path.join(os.getcwd(), folder_name)
        os.makedirs(folder_path, exist_ok=True) # Create the data folder if it doesn't exist, or do nothing if it does
        print(f"Data folder created or already exists at: {folder_path}")
        return folder_path
    except Exception as e:
        print(f"An error occurred while setting up the data folder: {e}")
        return None

# Other helper functions can be added here