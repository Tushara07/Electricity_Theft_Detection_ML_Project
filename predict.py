import pandas as pd
import joblib

def detect_theft(data):

    # load trained model
    model = joblib.load("models/theft_model.pkl")

    # clean column names
    data.columns = data.columns.str.strip()

    # remove ID and label columns safely
    X = data.drop(columns=["CONS_NO", "FLAG"], errors="ignore")

    # convert all values to numeric
    X = X.apply(pd.to_numeric, errors="coerce")

    # handle missing values
    X = X.fillna(0)

    # ensure feature order matches training
    X = X.iloc[:, :model.n_features_in_]

    # predict anomalies
    predictions = model.predict(X)

    data["Prediction"] = predictions
    data["Prediction"] = data["Prediction"].map({1: "Normal", -1: "Suspicious"})

    return data