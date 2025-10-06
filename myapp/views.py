from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages

def home(request):
    return render(request, 'myapp/home.html')

def about(request):
    return render(request, 'myapp/about_us.html')

def contact(request):
    return render(request, 'myapp/contact_us.html')

def logout_view(request):
    logout(request)
    messages.success(request, "You have been successfully logged out.")
    return redirect('home')

def check_auth(request):
    if request.user.is_authenticated:
        if request.user.is_doctor:
            return redirect('doctor_dashboard')
        elif request.user.is_patient:
            return redirect('patient_dashboard')
        elif request.user.is_superuser:
            return redirect('admin_dashboard')
    return redirect('home')
