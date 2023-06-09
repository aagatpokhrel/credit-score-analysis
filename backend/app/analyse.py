import pandas as pd
from sklearn.linear_model import LinearRegression

# linear regression model
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

# preprocess the data
def preprocess(input_data):
    # drop the columns that are not required
    columns_to_drop = ['fullName','address','phoneNumber','dateOfBirth','ssn']
    input_data = input_data.drop(columns_to_drop,axis=1)
    input_data['maritalStatus'] = input_data['maritalStatus'].map({'married':2,'single':1}) 
    input_data['isHomeOwner'] = input_data['isHomeOwner'].map({True:1,False:0})
    return input_data

# generate the report
def generate_report(input_data):
    # read the data
    data = pd.read_csv('credit.csv')

    # preprocess the data
    new_input_data = pd.DataFrame(input_data,index=[0])
    processed_input_data = preprocess(new_input_data)
    # call the predict function
    predicted_data = predict(data, processed_input_data)
    # create the report
    report = {
        "personal_details": {
            "name": input_data["fullName"],
            "address": input_data["address"],
            "phone_number": input_data["phoneNumber"],
            "age": input_data["dateOfBirth"],
            "seniority": input_data["seniority"],
        },

        "financial_details": {
            "ssn": input_data["ssn"],
            "income": input_data["income"],
            "expenses": input_data["expenses"],
            "assets": input_data["assets"],
            "debt": input_data["debt"],
            "score": predicted_data[0],
        }
    }
    # return the report and score
    return report, predicted_data[0]

