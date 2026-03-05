import pandas as pd
import joblib

def detect_theft(data):

    # load trained model
    model = joblib.load("models/theft_model.pkl")

    # remove ID and label columns
    X = data.drop(["CONS_NO", "FLAG"], axis=1)

    # handle missing values
    X = X.fillna(X.mean())

    # predict anomalies
    predictions = model.predict(X)

    # convert prediction values
    data["Prediction"] = predictions
    data["Prediction"] = data["Prediction"].map({1: "Normal", -1: "Suspicious"})

    return data