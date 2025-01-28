import pathlib
from pathlib import Path
import datetime
import json
from json import JSONDecodeError
import os


def log_errors(error_message):
    current_dir = Path.cwd()
    log_file_path = current_dir / "data" / "error_log.json"
    
    try:
        log_file_path = Path(log_file_path)
        if log_file_path.exists():
            with open(log_file_path, 'a') as file:
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

def setup_emails():
    try: 
        current_dir = Path.cwd()
        with open (Path(current_dir / "data" / "emails.json"),"w") as f:
            data = {}
            f.dumps(data)
    except Exception as e:
        error = f"An uexpected error occured: {e}"
        log_errors(error)
    return Path(current_dir / "data" / "emails.json")

    

def setup():
    try:
        current_dir = Path.cwd()

        # Create the log file path in the parent directory
        log_file_path = current_dir / "data"
        os.makedirs(log_file_path, exist_ok=True) # Create the data folder if it doesn't exist, or do nothing if it does
        
        print(f"Data folder created or already exists at: {log_file_path}")
        return log_file_path
    except Exception as e:
        print(f"An error occurred while setting up the data folder: {e}")
        return None

# Other helper functions can be added here