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
