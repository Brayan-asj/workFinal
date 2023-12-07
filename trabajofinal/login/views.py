from django.shortcuts import render

# Create your views here.

def fLogin(request):
    return render(request, "login.html")

def landing(request):
    return render(request, 'landingpage.html')