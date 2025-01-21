import json
import datetime
import os

def log_errors(error_message):
    try:
        log_file_path = os.path.join(os.getcwd(), 'data', 'error_log.json')
        with open(log_file_path, 'a') as file:
            data = {
                'timestamp': str(datetime.datetime.now()),
                'error_message': error_message
            }
            json.dump(data, file, indent=4)
        return True
    except Exception as e:
        print(f"An error occurred while trying to log errors: {e}")
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