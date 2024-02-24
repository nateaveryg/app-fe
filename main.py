from flask import Flask, render_template
import jinja2
import datetime
import requests
import os

app = Flask(__name__)

@app.route("/")
def hello_world():
    today = datetime.date.today()
    return render_template("hello_world.html", today=today)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
