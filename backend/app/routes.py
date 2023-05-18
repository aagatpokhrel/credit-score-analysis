from app import app, db
from flask import jsonify, request
from app.models import User
from app.analyse import generate_report

import json


@app.route('/')
def index():
    return "Hello, World!"


@app.route('/credit-score', methods=['POST'])
def credit_score():
    data = request.get_json()
    if User.query.filter_by(social_security_number=data['ssn']).first():
        return jsonify({'message': 'User already exists!'})
    else:
        user = User(social_security_number=data['ssn'], name=data['fullName'], address=data['address'], phone_number=data['phoneNumber'], seniority=data['seniority'], home=data['isHomeOwner'], age=data['dateOfBirth'], marital=data['maritalStatus'], expenses=data['expenses'], income=data['income'], assets=data['assets'], debt=data['debt'], time=data['loanTaken'], times_paid_on_time=data['paidBeforeDeadline'], avg_overdue_time=data['averageOverdueTime'])
        report, score = generate_report(data)
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'User created successfully!', 'score': score, 'report': report})
    
@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    if query:
        user = User.query.filter_by(social_security_number=query).first()
        report, score = generate_report(user.return_dict())
        return jsonify({'message': 'User found!', 'score': score, 'report': report})
    else :
        return jsonify({'message': 'No user found!'})