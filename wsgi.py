from flask import Flask, render_template
application = Flask(__name__)

# @application.route("/")
# def hello():
#     return "Hello World! Webhook testing! Github Edit"


@application.route("/")
def template():
    return render_template("template.html")


@application.route("/home")
def home():
    return render_template("home.html")


@application.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    application.run()
