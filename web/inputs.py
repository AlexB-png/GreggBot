from flask import Flask, request, render_template
import pathlib
from pathlib import Path
import random as r
import json

# flask constructor
app = Flask(__name__)
# a decorator used to tell the application
# which URL is associated function
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/email_input', methods=["POST"])
def get_email_input():
    if request.method == "POST":
        # getting input with email = get_email)input in HTML form
        email = request.form.get("email")
        current_dir = Path.cwd()
        data_file = Path(current_dir / "web" / "static" / "emails.json")
        with open(data_file, 'r') as file:
            data = json.load(file)
        with open(data_file, 'w') as file:
            key = r.randint(100000000, 999999999)
            if key not in data:
                data[key] = {}
                data[key]["email"] = email
                data[key]["uses"] = 0
            
    else:
        print("idk what has gone wrong but something has")

    return render_template("index.html")

@app.route('/new_link')
def get_new_link():
    if request.method == "GET":
        return render_template("new_link.html")
    else:
        print("idk what has gone wrong but something has")

