from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, DoctorProfile, PatientProfile, HeartDiseasePrediction
from django.core.validators import RegexValidator

class DoctorSignupForm(UserCreationForm):
    full_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone_number = forms.CharField(
        validators=[RegexValidator(
            regex=r'^\+?1?\d{9,15}$',
            message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
        )]
    )
    medical_license_number = forms.CharField(max_length=50)
    specialization = forms.CharField(max_length=100)
    years_of_experience = forms.IntegerField(
        min_value=0,
        max_value=50
    )
    education = forms.CharField(
        widget=forms.Textarea,
        help_text='Enter your medical education details'
    )
    hospital_clinic = forms.CharField(
        max_length=200,
        required=False
    )
    address = forms.CharField(
        widget=forms.Textarea,
        required=False
    )
    consultation_fee = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        required=False
    )
    available_days = forms.CharField(
        max_length=200,
        required=False
    )
    available_timings = forms.CharField(
        max_length=200,
        required=False
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2', 'full_name', 'email', 'phone_number',
                 'medical_license_number', 'specialization', 'years_of_experience',
                 'education', 'hospital_clinic', 'address', 'consultation_fee',
                 'available_days', 'available_timings')

    def save(self, commit=True):
        user = super().save(commit=False)
        # Split full name into first and last name
        name_parts = self.cleaned_data['full_name'].split(' ', 1)
        user.first_name = name_parts[0]
        user.last_name = name_parts[1] if len(name_parts) > 1 else ''
        user.email = self.cleaned_data['email']
        user.phone_number = self.cleaned_data['phone_number']
        user.user_type = 'doctor'
        if commit:
            user.save()
        return user

class SimplePatientSignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(
        required=True,
        validators=[RegexValidator(
            regex=r'^\+?1?\d{9,15}$',
            message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
        )]
    )
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone_number', 'first_name', 'last_name', 'password1', 'password2')
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.phone_number = self.cleaned_data['phone_number']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.user_type = 'patient'
        if commit:
            user.save()
        return user

class SimpleDoctorSignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(
        required=True,
        validators=[RegexValidator(
            regex=r'^\+?1?\d{9,15}$',
            message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
        )]
    )
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    medical_license_number = forms.CharField(max_length=100, required=True)
    specialization = forms.CharField(max_length=100, required=True)
    dob = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={'type': 'date'}),
        help_text='Please enter your date of birth'
    )
    gender = forms.ChoiceField(
        choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')],
        required=True
    )
    
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone_number', 'first_name', 'last_name', 
                 'medical_license_number', 'specialization', 'dob', 'gender', 'password1', 'password2')
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.phone_number = self.cleaned_data['phone_number']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.user_type = 'doctor'
        if commit:
            user.save()
        return user

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']

