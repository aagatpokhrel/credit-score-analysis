from app import app, db
from flask import jsonify, request

import json


@app.route('/')
def index():
    return "Hello, World!"

@app.route('/credit-score', methods=['POST'])
def credit_score():
    data = request.get_json()
    print(data)
    