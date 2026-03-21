from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta

app = Flask(__name__)

@app.route("/",methods = ["POST","GET"])
def main():
    text_output = ""
    if request.method == "POST":
        user_input = request.form["user_input"]
        text_output = user_input # display what the user typed out onto the screen

    return render_template("index.html",output = text_output)
if __name__ == "__main__":
    app.run(debug=True) 