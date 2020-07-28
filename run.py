import os
from datetime import datetime
from flask import Flask, json, redirect, render_template, request, session, url_for, flash


app = Flask(__name__)
app.secret_key = "randomstring123"
messages = []
app = Flask(__name__)
app.secret_key = 'some_secret'


@app.route('/')
def index():
    return render_template("index.html", page_title="Ananya Caterers")


def add_message(username, message):
    """Add messages to the `messages` list"""
    now = datetime.now().strftime("%H:%M:%S")
    messages.append({"timestamp": now, "from": username, "message": message})
    


@app.route("/", methods=["GET", "POST"])
def chat():
    """Main page with instructions"""
    if request.method == "POST":
        session["username"] = request.form["username"]
        f = open("chathistory.txt", 'w')

    if "username" in session:
        return redirect(url_for("user", username=session["username"]))

    return render_template("index.html")


@app.route("/chat/<username>", methods=["GET", "POST"])
def user(username):
    """Add and display chat messages"""
    if request.method == "POST":
        username = session["username"]
        message = request.form["message"]
        add_message(username, message)
        return redirect(url_for("user", username=session["username"]))
    return render_template("chat.html", username=username, chat_messages=messages, page_title="Chat with Us")



@app.route("/ourspecialities")
def ourspecialities():
    data = []
    with open("data/dishes.json","r") as json_data:
        data = json.load(json_data)
    return render_template("ourspecialities.html", page_title="Our Specialities", dishes =data)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method =="POST":
        flash("Thank you {}, we have recieved your message!".format(request.form["name"]))
    return render_template ("contact.html", page_title = "Contact Us")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title = "Come work with us")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=False)

