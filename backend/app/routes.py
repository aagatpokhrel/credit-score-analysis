from app import app, db
from flask import jsonify, request
from app.models import User
from app.analyse import generate_report

import json

# this function is called when the user hits the home page (test purposes)
@app.route('/')
def index():
    return "Hello, World!"

# this function is called when the user clicks on the submit button on the form
@app.route('/credit-score', methods=['POST'])
def credit_score():
    data = request.get_json()
    # check if the user already exists in the database
    if User.query.filter_by(social_security_number=data['ssn']).first():
        return jsonify({'message': 'User already exists!'})
    else:
        # if the user does not exist then create a new user and add it to the database
        user = User(social_security_number=data['ssn'], name=data['fullName'], address=data['address'], phone_number=data['phoneNumber'], seniority=data['seniority'], home=data['isHomeOwner'], age=data['dateOfBirth'], marital=data['maritalStatus'], expenses=data['expenses'], income=data['income'], assets=data['assets'], debt=data['debt'], time=data['loanTaken'], times_paid_on_time=data['paidBeforeDeadline'], avg_overdue_time=data['averageOverdueTime'])
        # generate the report and score for the user
        report, score = generate_report(data)
        db.session.add(user)
        db.session.commit()
        # return the report and score to the frontend
        return jsonify({'message': 'User created successfully!', 'score': score, 'report': report})

# search through the search bar hits this function and performs the activiies
@app.route('/search', methods=['GET'])
def search():
    #seach query is taken from the search bar
    query = request.args.get('query')
    #if query is not empty then search for the user
    if query:
        user = User.query.filter_by(social_security_number=query).first()
        report, score = generate_report(user.return_dict())
        return jsonify({'message': 'User found!', 'score': score, 'report': report})
    else :
        return jsonify({'message': 'No user found!'})