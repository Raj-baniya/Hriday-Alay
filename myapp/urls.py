from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    # Navigation
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    # Doctor URLs
    path('doctor_signup/', views.doctor_signup, name='doctor_signup'),
    path('simple_doctor_signup/', views.simple_doctor_signup, name='simple_doctor_signup'),
    path('doctor/login/', views.doctor_login, name='doctorlogin'),
    path('doctor/dashboard/', views.doctor_dashboard, name='doctor_dashboard'),

    # Patient URLs
    path('patient_signup/', views.patient_signup, name='patient_signup'),
    path('simple_patient_signup/', views.simple_patient_signup, name='simple_patient_signup'),
    path('login/', views.login_view, name='login'),
    path('register/', views.home, name='register'),  # Redirect to home page for registration options
    path('patientlogin/', views.patient_login, name='patientlogin'),
    path('patient_dashboard/', views.patient_dashboard, name='patient_dashboard'),

    # Admin URLs
    path('admin/login/', views.admin_login, name='adminlogin'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),

    # Emergency Services
    path('video_call/', views.video_call, name='video_call'),
    path('recommendation_dashboard/', views.recommendation_dashboard, name='recommendation_dashboard'),
    path('location_recommendation/', views.location_recommendation, name='location_recommendation'),
    path('food_recommendation/', views.food_recommendation, name='food_recommendation'),
    path('ecg_data/', views.ecg_data, name='ecg_data'),

    # Authentication
    path('logout/', views.logout_view, name='logout'),

    path('health_data/', views.health_data, name='health_data'),
    path('heart_disease_prediction/', views.heart_disease_prediction, name='heart_disease_prediction'),
    path('implant_pricing/', views.implant_pricing, name='implant_pricing'),

    path('patient_search/', views.patient_search, name='patient_search'),
]