from flask import Flask, render_template
application = Flask(__name__)

# @application.route("/")
# def hello():
#     return "Hello World! Webhook testing! Github Edit"

@application.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    application.run()
