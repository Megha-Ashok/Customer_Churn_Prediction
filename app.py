from flask import Flask, request, jsonify, render_template
import numpy as np
import joblib
from tensorflow.keras.models import load_model

app = Flask(__name__)

# Load your saved model and scaler
model = load_model("churn_model.h5")
scaler = joblib.load("scaler.pkl")

# Helper to preprocess input
def preprocess_input(data):
    # Prepare input feature vector matching training features:
    # Order of features (example): CreditScore, Age, Tenure, Balance, NumOfProducts, HasCreditCard, IsActiveMember,
    # EstimatedSalary, Geography_Germany, Geography_Spain, Gender_Male

    geography_map = {
        "France": [0, 0],
        "Germany": [1, 0],
        "Spain": [0, 1]
    }
    gender_map = {
        "Female": 0,
        "Male": 1
    }

    geography_features = geography_map.get(data['geography'], [0,0])
    gender_feature = gender_map.get(data['gender'], 0)

    features = [
        float(data['creditScore']),
        float(data['age']),
        float(data['tenure']),
        float(data['balance']),
        float(data['numOfProducts']),
        float(data['hasCreditCard']),
        float(data['isActiveMember']),
        float(data['estimatedSalary']),
        geography_features[0],
        geography_features[1],
        gender_feature
    ]
    # Scale features
    features_scaled = scaler.transform([features])
    return features_scaled

@app.route('/')
def home():
    return render_template('index.html')  # your UI HTML file in templates/

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    # Preprocess
    X = preprocess_input(data)
    # Predict
    pred_prob = model.predict(X)[0][0]
    pred_class = int(pred_prob > 0.5)

    return jsonify({
        "churn_probability": float(pred_prob),
        "churn": bool(pred_class)
    })

if __name__ == '__main__':
    app.run(debug=True)
