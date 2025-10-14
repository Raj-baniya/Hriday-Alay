from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import CustomUser, DoctorProfile, PatientProfile, HeartDiseasePrediction
from .forms import DoctorSignupForm, SimplePatientSignupForm, CustomAuthenticationForm, HeartDiseasePredictionForm, SimpleDoctorSignupForm, PatientSearchForm
from django.contrib.auth.forms import AuthenticationForm
import pickle
import numpy as np
import os
import joblib
from pathlib import Path
from ml_model import predict_heart_disease  # Import the prediction function
from django.db import transaction
from django.utils import timezone
from django.contrib.auth.models import User

# Home Page
def home(request):
    return render(request, 'myapp/home.html')

# Doctor Signup
def doctor_signup(request):
    if request.method == 'POST':
        form = DoctorSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create doctor profile
            DoctorProfile.objects.create(
                user=user,
                medical_license_number=form.cleaned_data['medical_license_number'],
                specialization=form.cleaned_data['specialization'],
                years_of_experience=form.cleaned_data['years_of_experience'],
                education=form.cleaned_data['education'],
                hospital_clinic=form.cleaned_data['hospital_clinic'],
                address=form.cleaned_data['address'],
                consultation_fee=form.cleaned_data['consultation_fee'],
                available_days=form.cleaned_data['available_days'],
                available_timings=form.cleaned_data['available_timings']
            )
            messages.success(request, 'Account created successfully. Please login.')
            return redirect('login')
    else:
        form = DoctorSignupForm()
    return render(request, 'myapp/doctor_signup.html', {'form': form})

# Patient Signup
def patient_signup(request):
    if request.method == 'POST':
        form = SimplePatientSignupForm(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    # Create the user first
                    user = form.save()
                    print(f"User created successfully: {user.username}")
                    
                    # Create patient profile with only the fields that are provided
                    profile_data = {
                        'user': user,
                    }
                    
                    # Add optional fields only if they are provided
                    if 'dob' in form.cleaned_data and form.cleaned_data['dob']:
                        profile_data['dob'] = form.cleaned_data['dob']
                    
                    if 'gender' in form.cleaned_data and form.cleaned_data['gender']:
                        profile_data['gender'] = form.cleaned_data['gender']
                    
                    if 'blood_group' in form.cleaned_data and form.cleaned_data['blood_group']:
                        profile_data['blood_group'] = form.cleaned_data['blood_group']
                    
                    if 'height' in form.cleaned_data and form.cleaned_data['height']:
                        profile_data['height'] = form.cleaned_data['height']
                    
                    if 'weight' in form.cleaned_data and form.cleaned_data['weight']:
                        profile_data['weight'] = form.cleaned_data['weight']
                    
                    if 'medical_history' in form.cleaned_data and form.cleaned_data['medical_history']:
                        profile_data['medical_history'] = form.cleaned_data['medical_history']
                    
                    if 'allergies' in form.cleaned_data and form.cleaned_data['allergies']:
                        profile_data['allergies'] = form.cleaned_data['allergies']
                    
                    if 'current_medications' in form.cleaned_data and form.cleaned_data['current_medications']:
                        profile_data['current_medications'] = form.cleaned_data['current_medications']
                    
                    if 'emergency_contact' in form.cleaned_data and form.cleaned_data['emergency_contact']:
                        profile_data['emergency_contact'] = form.cleaned_data['emergency_contact']
                    
                    if 'emergency_relationship' in form.cleaned_data and form.cleaned_data['emergency_relationship']:
                        profile_data['emergency_relationship'] = form.cleaned_data['emergency_relationship']
                    
                    if 'emergency_phone' in form.cleaned_data and form.cleaned_data['emergency_phone']:
                        profile_data['emergency_phone'] = form.cleaned_data['emergency_phone']
                    
                    # Create the profile with only the provided fields
                    profile = PatientProfile.objects.create(**profile_data)
                    print(f"Patient profile created successfully: {profile.id}")
                    
                    messages.success(request, 'Account created successfully. Please login.')
                    return redirect('login')
            except Exception as e:
                print(f"Error during patient signup: {str(e)}")
                messages.error(request, f'Error creating account: {str(e)}')
                # If we get here, the transaction has been rolled back
        else:
            print("Form validation errors:", form.errors)
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = SimplePatientSignupForm()
    return render(request, 'myapp/patient_signup.html', {'form': form})

# Login Views
def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            
            # Redirect based on user type
            if user.is_superuser:
                return redirect('admin_dashboard')
            elif user.is_doctor:
                return redirect('doctor_dashboard')
            elif user.is_patient:
                return redirect('patient_dashboard')
            else:
                return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = CustomAuthenticationForm()
    return render(request, 'myapp/login.html', {'form': form})

def doctor_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.is_doctor:
                login(request, user)
                return redirect('doctor_dashboard')
            else:
                messages.error(request, "Invalid credentials for a doctor.")
    else:
        form = CustomAuthenticationForm()
    return render(request, 'myapp/doctorlogin.html', {'form': form})

def patient_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.is_patient:
                login(request, user)
                return redirect('patient_dashboard')
            else:
                messages.error(request, "Invalid credentials for a patient.")
    else:
        form = CustomAuthenticationForm()
    return render(request, 'myapp/patientlogin.html', {'form': form})

def admin_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.is_superuser:
                login(request, user)
                return redirect('admin_dashboard')
            else:
                messages.error(request, "You are not an admin.")
    else:
        form = AuthenticationForm()
    return render(request, 'myapp/adminlogin.html', {'form': form})

# Dashboards
@login_required
def doctor_dashboard(request):
    if not request.user.is_doctor:
        messages.error(request, "You don't have permission to access this page")
        return redirect('home')
    
    # Get the doctor's profile
    doctor_profile = DoctorProfile.objects.get(user=request.user)
    
    # Get today's appointments (you'll need to implement this model)
    today_appointments = []  # Replace with actual appointment query
    
    context = {
        'doctor_profile': doctor_profile,
        'today_appointments': today_appointments,
        'user': request.user,
    }
    
    return render(request, 'myapp/doctor_dashboard.html', context)

@login_required
def patient_dashboard(request):
    if not request.user.is_patient:
        messages.error(request, "You don't have permission to access this page")
        return redirect('home')
    
    # Get the patient's profile
    patient_profile = PatientProfile.objects.get(user=request.user)
    
    # Get today's appointments (you'll need to implement this model)
    recent_appointments = []  # Replace with actual appointment query
    
    # Calculate health score (example implementation)
    health_score = 85  # This should be calculated based on actual health metrics
    
    # Get next appointment
    next_appointment = None  # Replace with actual appointment query
    
    context = {
        'patient_profile': patient_profile,
        'recent_appointments': recent_appointments,
        'health_score': health_score,
        'next_appointment': next_appointment,
        'user': request.user,
    }
    
    return render(request, 'myapp/patient_dashboard.html', context)

@login_required
def admin_dashboard(request):
    if not request.user.is_superuser:
        messages.error(request, "You don't have permission to access this page")
        return redirect('home')
    return render(request, 'myapp/admin_dashboard.html')

# Navigation Pages
    return render(request, 'myapp/about_us.html')

def contact(request):
    return render(request, 'myapp/contact_us.html')

# Emergency Services
def video_call(request):
    return render(request, 'myapp/video_call.html')

def recommendation_dashboard(request):
    return render(request, 'myapp/recommendation_dashboard.html')

def location_recommendation(request):
    return render(request, 'myapp/location_recommendation.html')

def food_recommendation(request):
    return render(request, 'myapp/food_recommendation.html')

def ecg_data(request):
    return render(request, 'myapp/embedded_ECG.html')

# Logout
def logout_view(request):
    logout(request)
    messages.success(request, "You have been successfully logged out.")
    return redirect('home')

# Auth Redirect Helper (optional utility)
def check_auth(request):
    if request.user.is_authenticated:
        if request.user.is_doctor:
            return redirect('doctor_dashboard')
        elif request.user.is_patient:
            return redirect('patient_dashboard')
        elif request.user.is_superuser:
            return redirect('admin_dashboard')
    return redirect('home')

@login_required
def health_data(request):
    return render(request, 'myapp/health_data.html')  # Make sure this template exists

@login_required
def heart_disease_prediction(request):
    # Check if user is a patient
    if not request.user.is_patient:
        messages.error(request, "Only patients can access the prediction page.")
        return redirect('home')
    
    if request.method == 'POST':
        form = HeartDiseasePredictionForm(request.POST)
        if form.is_valid():
            try:
                # Get form data
                form_data = form.cleaned_data
                
                # Make prediction using the imported function
                prediction, probability = predict_heart_disease(form_data)
                
                if prediction is not None:
                    # Save prediction to database
                    HeartDiseasePrediction.objects.create(
                        patient=request.user,
                        prediction_result=bool(prediction),
                        probability=probability,
                        age=form_data['age'],
                        sex=form_data['sex'],
                        cp=form_data['cp'],
                        trestbps=form_data['trestbps'],
                        chol=form_data['chol'],
                        fbs=form_data['fbs'],
                        restecg=form_data['restecg'],
                        thalach=form_data['thalach'],
                        exang=form_data['exang'],
                        oldpeak=form_data['oldpeak'],
                        slope=form_data['slope'],
                        ca=form_data['ca'],
                        thal=form_data['thal']
                    )
                    
                    # Prepare result message
                    result_text = 'High Risk' if prediction == 1 else 'Low Risk'
                    
                    context = {
                        'form': form,
                        'result': result_text,
                        'probability': f'{probability:.2f}',
                        'prediction_saved': True
                    }
                    
                    messages.success(request, 'Prediction completed successfully!')
                    return render(request, 'myapp/heart_disease_prediction.html', context)
                else:
                    messages.error(request, 'Error making prediction. Please try again.')
            except Exception as e:
                messages.error(request, f'An error occurred: {str(e)}')
        else:
            messages.error(request, 'Please correct the errors in the form.')
    else:
        form = HeartDiseasePredictionForm()
    
    return render(request, 'myapp/heart_disease_prediction.html', {'form': form})

@login_required
@login_required
def patient_search(request):
    """View for searching patients and viewing their heart disease predictions."""
    # Check if the user is a doctor
    if not request.user.is_doctor:
        messages.error(request, "Only doctors can access patient records.")
        return redirect('home')
    
    search_query = request.GET.get('q', '')
    patient = None
    heart_predictions = None
    error_message = None
    form = PatientSearchForm(initial={'username': search_query})

    if search_query:
        try:
            # Get the patient user
            patient_user = CustomUser.objects.get(username=search_query)
            if not patient_user.is_patient:
                error_message = "The user found is not a patient."
                patient = None
            else:
                # Get the patient profile
                patient = PatientProfile.objects.get(user=patient_user)
                # Get heart disease predictions
                heart_predictions = HeartDiseasePrediction.objects.filter(
                    patient=patient_user
                ).order_by('-prediction_date')
        except CustomUser.DoesNotExist:
            error_message = "No patient found with the given username."
        except PatientProfile.DoesNotExist:
            error_message = "Patient profile not found."

    context = {
        'form': form,
        'search_query': search_query,
        'patient': patient,
        'heart_predictions': heart_predictions,
        'error_message': error_message,
    }
    return render(request, 'myapp/patient_search.html', context)
