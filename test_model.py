from ml_model import load_model, predict_heart_disease

def test_model():
    # Test model loading
    model, scaler = load_model()
    if model is None or scaler is None:
        print("Error: Failed to load model or scaler")
        return

    print("Model and scaler loaded successfully!")

    # Test prediction with sample data
    sample_data = {
        'age': 45,
        'sex': 1,
        'cp': 0,
        'trestbps': 130,
        'chol': 250,
        'fbs': 0,
        'restecg': 0,
        'thalach': 150,
        'exang': 0,
        'oldpeak': 2.3,
        'slope': 0,
        'ca': 0,
        'thal': 1
    }

    prediction, probability = predict_heart_disease(sample_data)
    if prediction is None or probability is None:
        print("Error: Failed to make prediction")
        return

    print(f"Prediction: {'High Risk' if prediction == 1 else 'Low Risk'}")
    print(f"Probability: {probability}%")

if __name__ == "__main__":
    test_model() 