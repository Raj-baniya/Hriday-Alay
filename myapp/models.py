from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('doctor', 'Doctor'),
        ('patient', 'Patient'),
    )
    
    # Phone number validator
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    phone_number = models.CharField(
        max_length=15,
        validators=[phone_regex],
        blank=True,
        null=True
    )
    
    # Add any additional fields needed for both doctors and patients
    
    @property
    def is_doctor(self):
        return self.user_type == 'doctor'
    
    @property
    def is_patient(self):
        return self.user_type == 'patient'
    
    def __str__(self):
        return f"{self.username} ({self.get_user_type_display()})"


class DoctorProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='doctor_profile')
    dob = models.DateField()
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    medical_license_number = models.CharField(max_length=100, unique=True)
    specialization = models.CharField(max_length=100)
    years_of_experience = models.PositiveIntegerField()
    hospital_name = models.CharField(max_length=100, blank=True, null=True)
    license_document = models.FileField(upload_to='doctor_licenses/', blank=True, null=True)
    
    # New fields
    education = models.TextField(blank=True, null=True)
    certifications = models.TextField(blank=True, null=True)
    languages_spoken = models.CharField(max_length=200, blank=True, null=True)
    consultation_fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    available_days = models.CharField(max_length=100, blank=True, null=True)
    available_hours = models.CharField(max_length=100, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='doctor_profiles/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"


class PatientProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='patient_profile')
    dob = models.DateField(null=True, blank=True)  # Make it nullable temporarily
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)  # Make it nullable temporarily
    
    # Basic Information
    blood_group = models.CharField(max_length=5, blank=True, null=True)
    height = models.FloatField(blank=True, null=True)  # in cm
    weight = models.FloatField(blank=True, null=True)  # in kg
    profile_picture = models.ImageField(upload_to='patient_profiles/', blank=True, null=True)
    
    # Medical Information
    medical_history = models.TextField(blank=True, null=True)
    allergies = models.TextField(blank=True, null=True)
    current_medications = models.TextField(blank=True, null=True)
    last_checkup = models.DateField(blank=True, null=True)
    
    # Emergency Contacts
    emergency_contact = models.CharField(max_length=100, blank=True, null=True)
    emergency_relationship = models.CharField(max_length=50, blank=True, null=True)
    emergency_phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"


class HeartDiseasePrediction(models.Model):
    patient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='heart_predictions')
    prediction_date = models.DateTimeField(auto_now_add=True)
    prediction_result = models.BooleanField()  # True for positive, False for negative
    probability = models.FloatField()  # Probability of having heart disease
    # Input features
    age = models.IntegerField()
    sex = models.IntegerField()  # 0 for female, 1 for male
    cp = models.IntegerField()  # Chest pain type
    trestbps = models.IntegerField()  # Resting blood pressure
    chol = models.IntegerField()  # Serum cholesterol
    fbs = models.IntegerField()  # Fasting blood sugar
    restecg = models.IntegerField()  # Resting electrocardiographic results
    thalach = models.IntegerField()  # Maximum heart rate achieved
    exang = models.IntegerField()  # Exercise induced angina
    oldpeak = models.FloatField()  # ST depression induced by exercise
    slope = models.IntegerField()  # Slope of the peak exercise ST segment
    ca = models.IntegerField()  # Number of major vessels
    thal = models.IntegerField()  # Thalassemia

    def __str__(self):
        return f"Prediction for {self.patient.username} on {self.prediction_date}"

    class Meta:
        ordering = ['-prediction_date']