from flask import Flask, render_template
import os
import mainfunctions
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret123'  # Replace with a secure key


def get_api_key(filename):
    all_keys= mainfunctions.read_from_file("api_key.json") #Read the contents of the JSON file
    return all_keys["aqi_api_key"]
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True, port=7070)
