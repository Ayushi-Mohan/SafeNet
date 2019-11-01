from django.shortcuts import render


def index(request):
    return render(request,'safenet/index.html')

def plan_info(request):
    return render(request,'safenet/plan_info.html')

def login(request):
    return render(request,'safenet/login.html')

def signup(request):
    return render(request,'safenet/signup.html')
