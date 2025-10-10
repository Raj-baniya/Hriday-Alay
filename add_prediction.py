import os
import django
from django.utils import timezone

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from myapp.models import CustomUser, HeartDiseasePrediction

# Get Rahul Verma's user object
patient = CustomUser.objects.get(username='rahul_verma')

# Create the prediction
prediction = HeartDiseasePrediction.objects.create(
    patient=patient,
    prediction_date=timezone.now(),
    prediction_result=True,
    probability=75.5,
    age=35,
    sex=1,
    cp=1,
    trestbps=145,
    chol=220,
    fbs=0,
    restecg=1,
    thalach=155,
    exang=1,
    oldpeak=1.5,
    slope=1,
    ca=1,
    thal=1
)

print(f"Created prediction for {patient.get_full_name()}")
print(f"Prediction Result: {'High Risk' if prediction.prediction_result else 'Low Risk'}")
print(f"Probability: {prediction.probability}%") 