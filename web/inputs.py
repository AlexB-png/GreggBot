from flask import Flask, request, render_template

# flask constructor
app = Flask(__name__)
# a decorator used to tell the application
# which URL is associated function
@app.route('/')
def website():
    return render_template("index.html")

@app.route('/email_input', methods=["POST"])
def get_email_input():
    if request.method == "POST":
        # getting input with email = get_email)input in HTML form
        email = request.form.get("email")
        return email
    else:
        print("idk what has gone wrong but something has")

if __name__=='__main__':
    app.run()