from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})

app.config['SECRET_KEY'] = "credit-analysis"
app.config['CORS_HEADERS'] = 'Content-Type'

from app import routes