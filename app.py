from flask import Flask
import os
import mainfunctions
import requests

url = "D"


def get_api_key(filename):
    all_keys= mainfunctions.read_from_file("api_key.json") #Read the contents of the JSON file
    return all_keys["aqi_api_key"]
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True, port=7070)
