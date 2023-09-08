from flask import Flask, request
from flask_cors import CORS
import psycopg2

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["POST", "GET"])
def hello_world():
    return "hello world!"