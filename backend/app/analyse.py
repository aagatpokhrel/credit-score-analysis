import pandas as pd
from sklearn.linear_model import LinearRegression

def predict(data , new_input_data):

    # Separate the input features (X) and the target variable (y)
    X = data.drop('Score',axis=1)
    y = data['Score']

    # Create an instance of the LinearRegression model
    model = LinearRegression()

    # Fit the model to the data
    model.fit(X, y)
    prediction = model.predict(new_input_data)
    return prediction

def preprocess(input_data):
    columns_to_drop = ['fullName','address','phoneNumber','dateOfBirth','ssn']
    input_data = input_data.drop(columns_to_drop,axis=1)
    input_data['maritalStatus'] = input_data['maritalStatus'].map({'married':2,'single':1}) 
    input_data['isHomeOwner'] = input_data['isHomeOwner'].map({True:1,False:0})
    return input_data

def generate_report(input_data):
    data = pd.read_csv('credit.csv')
    new_input_data = pd.DataFrame(input_data,index=[0])
    processed_input_data = preprocess(new_input_data)
    predicted_data = predict(data, processed_input_data)
    report = {
        "name": input_data["fullName"],
        "address": input_data["address"],
        "score": predicted_data[0],
        "seniority": input_data["seniority"],
        "age": input_data["dateOfBirth"],
    }

    print(predicted_data[0])
    return report, predicted_data[0]

