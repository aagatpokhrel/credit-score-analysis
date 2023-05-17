import pandas as pd
from sklearn.linear_model import LinearRegression

def predict(input_data):
    # Load the CSV file
    data = pd.read_csv('credit.csv')
    new_input_data = pd.DataFrame(input_data)

    # Separate the input features (X) and the target variable (y)
    X = data.drop('Score', axis=1)
    y = data['Score']

    # Create an instance of the LinearRegression model
    model = LinearRegression()

    # Fit the model to the data
    model.fit(X, y)
    prediction = model.predict(new_input_data)
    return prediction

def generate_report(input_data):
    predicted_data = predict(input_data)
    report = {
        "name": input_data["name"],
        "address": input_data["address"],
        "score": predicted_data,
        "credit_status": input_data["credit_status"],
        "seniority": input_data["seniority"],
        "home": input_data["home"],
        "age": input_data["age"]
    }

    return report, predicted_data

