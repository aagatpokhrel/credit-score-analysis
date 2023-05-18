from app import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    address = db.Column(db.String(100))
    phone_number = db.Column(db.String(20))
    social_security_number = db.Column(db.String(100))
    seniority = db.Column(db.Integer)
    home = db.Column(db.Boolean)
    age = db.Column(db.Integer)
    marital = db.Column(db.String(50))
    expenses = db.Column(db.Float)
    income = db.Column(db.Float)
    assets = db.Column(db.Float)
    debt = db.Column(db.Float)
    time = db.Column(db.Integer)
    times_paid_on_time = db.Column(db.Integer)
    avg_overdue_time = db.Column(db.Float)

    def __init__(self, social_security_number, name, address, phone_number, seniority, home, age,
                 marital, expenses, income, assets, debt, time, times_paid_on_time, avg_overdue_time):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.social_security_number = social_security_number
        self.seniority = seniority
        self.home = home
        self.age = age
        self.marital = marital
        self.expenses = expenses
        self.income = income
        self.assets = assets
        self.debt = debt
        self.time = time
        self.times_paid_on_time = times_paid_on_time
        self.avg_overdue_time = avg_overdue_time

    def return_dict(self):
        return {
            "fullName": self.name,
            "address": self.address,
            "phoneNumber": self.phone_number,
            "ssn": self.social_security_number,
            "seniority": self.seniority,
            "isHomeOwner": self.home,
            "dateOfBirth": self.age,
            "maritalStatus": self.marital,
            "expenses": self.expenses,
            "income": self.income,
            "assets": self.assets,
            "debt": self.debt,
            "loanTaken": self.time,
            "paidBeforeDeadline": self.times_paid_on_time,
            "averageOverdueTime": self.avg_overdue_time
        }