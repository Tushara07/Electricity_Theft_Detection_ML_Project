import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

# load dataset
DATA_URL = "https://drive.google.com/uc?export=download&id=1qbxrzKoLmHbXU3qUJMLr6QW0LUiseRg4"
data = pd.read_csv(DATA_URL)

print("Dataset loaded successfully")
print(data.shape)

# remove ID and label columns
X = data.drop(["CONS_NO", "FLAG"], axis=1)

# handle missing values
X = X.fillna(X.mean())

print("Training model...")

# train anomaly detection model
model = IsolationForest(contamination=0.1, random_state=42)
model.fit(X)

# save model
joblib.dump(model, "models/theft_model.pkl")

print("Model saved successfully!")