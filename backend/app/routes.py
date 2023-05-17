from app import app
from flask import jsonify, request

import json


@app.route('/')
def index():
    return "Hello, World!"

