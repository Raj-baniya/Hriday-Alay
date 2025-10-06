from django.shortcuts import render, redirect
from django.contrib import messages

def home(request):
    return render(request, 'myapp/home.html')

def about(request):
    return render(request, 'myapp/about_us.html')

def contact(request):
    return render(request, 'myapp/contact_us.html')
