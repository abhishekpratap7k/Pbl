from django.shortcuts import render


def login(req):
    return render(req,'index.html')
def signup(req):
    return render(req,'signup.html')
def otp(req):
    return render(req,'otp.html')
