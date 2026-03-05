import pandas as pd
import joblib

def detect_theft(data):

    model = joblib.load("models/theft_model.pkl")

    # clean column names
    data.columns = data.columns.str.strip()

    # remove ID and label columns safely
    X = data.drop(columns=["CONS_NO", "FLAG"], errors="ignore")

    # handle missing values
    X = X.fillna(X.mean())

    # predict anomalies
    predictions = model.predict(X)

    data["Prediction"] = predictions
    data["Prediction"] = data["Prediction"].map({1: "Normal", -1: "Suspicious"})

    return data