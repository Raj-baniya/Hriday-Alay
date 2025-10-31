# Heart Disease Prediction System

This is a Django-based web application that predicts the likelihood of heart disease based on various health parameters using machine learning.

## Features

- User authentication (login/register) for patients and doctors
- Heart disease prediction using machine learning
- Prediction history tracking
- Doctor dashboard for patient monitoring
- Patient search functionality
- Modern and responsive UI with Bootstrap 5

## Project Structure

```
myproject/
├── myapp/                  # Main Django application
│   ├── migrations/         # Database migrations
│   ├── templates/          # HTML templates
│   ├── static/             # Static files (CSS, JS, images)
│   ├── models.py           # Database models
│   ├── views.py            # View functions
│   ├── forms.py            # Form definitions
│   └── urls.py             # URL patterns
├── ml_model/               # Machine learning model
│   ├── models/             # Trained model files
│   ├── train.py            # Model training script
│   └── __init__.py         # Model loading and prediction functions
├── manage.py               # Django management script
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

## Setup Instructions

1. Clone the repository:

```bash
git clone <repository-url>
cd myproject
```

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Train the machine learning model:

```bash
python ml_model/train.py
```

5. Apply database migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

6. Create a superuser:

```bash
python manage.py createsuperuser
```

7. Run the development server:

```bash
python manage.py runserver
```

8. Access the application at http://localhost:8000

## Usage

### For Patients:

1. Register a new account or login with existing credentials
2. Navigate to the Heart Disease Prediction page
3. Enter the required health parameters
4. Submit the form to get the prediction
5. View prediction history in your profile

### For Doctors:

1. Login with doctor credentials
2. Access the doctor dashboard
3. Search for patients by username
4. View patient details and heart disease predictions
5. Monitor patient health trends

## Machine Learning Model

The heart disease prediction model is based on a Random Forest Classifier trained on the UCI Heart Disease dataset. The model uses the following features:

- Age
- Sex (0: Female, 1: Male)
- Chest Pain Type (0-3)
- Resting Blood Pressure
- Serum Cholesterol
- Fasting Blood Sugar
- Resting ECG Results
- Maximum Heart Rate
- Exercise Induced Angina
- ST Depression
- Slope of ST Segment
- Number of Major Vessels
- Thalassemia

For detailed information about the machine learning model, see `ml_model_documentation.txt`.

## Technologies Used

- Django 4.2+
- scikit-learn 1.2+
- NumPy 1.24+
- Pandas 2.0+
- Bootstrap 5
- HTML/CSS/JavaScript
- Python 3.8+

## Troubleshooting

If you encounter any issues during setup:

1. Ensure all dependencies are installed correctly
2. Check if the machine learning model is trained properly
3. Verify database migrations are applied
4. Check Django settings for any configuration issues

## License

This project is licensed under the MIT License - see the LICENSE file for details.
