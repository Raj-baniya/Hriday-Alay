import numpy as np
import pickle
import os

# Get the absolute path to the model file
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, 'ml_model', 'models', 'heart_disease_model.pkl')

def load_model():
    """Load the trained model and scaler from the pickle file."""
    try:
        with open(MODEL_PATH, 'rb') as f:
            model_data = pickle.load(f)
            return model_data['model'], model_data['scaler']
    except FileNotFoundError:
        print(f"Model file not found at: {MODEL_PATH}")
        return None, None
    except Exception as e:
        print(f"Error loading model: {str(e)}")
        return None, None

# Load the model and scaler
model, scaler = load_model()

def preprocess_input(data):
    """
    Convert form input data into a NumPy array suitable for model prediction.
    Ensures all values are properly formatted and scaled.
    """
    if scaler is None:
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
    if model is None:
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

__all__ = ['predict_heart_disease', 'load_model', 'preprocess_input']
