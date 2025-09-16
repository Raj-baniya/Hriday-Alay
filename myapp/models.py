from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'patient'),
        (2, 'doctor'),
        (3, 'admin'),
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=1)
    
    @property
    def is_patient(self):
        return self.user_type == 1
        
    @property
    def is_doctor(self):
        return self.user_type == 2

class DoctorProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='doctor_profile')
    medical_license_number = models.CharField(max_length=50, unique=True)
    specialization = models.CharField(max_length=100)
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, blank=True)
    profile_pic = models.ImageField(upload_to='doctor_profiles/', null=True, blank=True)

    def __str__(self):
        return f"Dr. {self.user.get_full_name() or self.user.username}"

class PatientProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='patient_profile')
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, blank=True)
    profile_pic = models.ImageField(upload_to='patient_profiles/', null=True, blank=True)

    def __str__(self):
        return f"Patient: {self.user.get_full_name() or self.user.username}"
