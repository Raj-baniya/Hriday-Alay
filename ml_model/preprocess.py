import numpy as np
import joblib
import os

# Load the trained model and scaler
MODEL_DIR = os.path.join(os.path.dirname(__file__), 'models')
MODEL_PATH = os.path.join(MODEL_DIR, 'heart_disease_model.pkl')
SCALER_PATH = os.path.join(MODEL_DIR, 'scaler.pkl')

try:
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
except FileNotFoundError:
    print("Model or scaler not found. Please run train.py first.")
    model = None
    scaler = None

def preprocess_input(data):
    """
    Convert form input data into a NumPy array suitable for model prediction.
    Ensures all values are properly formatted and scaled.
    """
    if model is None or scaler is None:
        return None

    try:
        # Convert input data to array
        input_array = np.array([
            float(data['age']),
            float(data['sex']),
            float(data['cp']),
            float(data['trestbps']),
            float(data['chol']),
            float(data['fbs']),
            float(data['restecg']),
            float(data['thalach']),
            float(data['exang']),
            float(data['oldpeak']),
            float(data['slope']),
            float(data['ca']),
            float(data['thal'])
        ]).reshape(1, -1)
        
        # Scale the input data
        scaled_data = scaler.transform(input_array)
        return scaled_data
    except (ValueError, KeyError) as e:
        print(f"Error preprocessing input: {str(e)}")
        return None

def predict_heart_disease(data):
    """
    Takes input data, preprocesses it, and returns the prediction result.
    Returns:
        tuple: (prediction, probability)
            prediction: 1 for high risk, 0 for low risk
            probability: percentage risk of heart disease
    """
    if model is None or scaler is None:
        return None, None

    processed_data = preprocess_input(data)
    if processed_data is None:
        return None, None

    try:
        prediction = model.predict(processed_data)[0]
        probability = model.predict_proba(processed_data)[0][1] * 100
        return int(prediction), round(probability, 2)
    except Exception as e:
        print(f"Error making prediction: {str(e)}")
        return None, None
