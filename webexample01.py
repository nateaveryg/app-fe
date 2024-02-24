from flask import Flask, render_template
import jinja2
import datetime
import requests

app = Flask(__name__)

@app.route("/")
def hello_world():
    today = datetime.date.today()
    return render_template("hello_world.html", today=today)

if __name__ == "__main__":
    app.run()

@app.route("/hello_api")
def hello_api():
    # Make a request to the service-a API.
    response = requests.get('http://localhost:8080/hello')

    # Parse the JSON response.
    data = response.json()

    # Display the JSON data in a web browser.
    print(data)

    return "Hello from the API!"