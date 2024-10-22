from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
import re
import random


def login_view(req):
    if req.method == "GET":
        return render(req, "login.html")
    cred = req.POST
    username = cred.get("username", "")
    password = cred.get("password", "")

    if not User.objects.filter(username=username).exists():
        messages.add_message(req, messages.WARNING, "No user found!")
        return redirect("Login")
    user = authenticate(request=req, username=username, password=password)
    if not user:
        messages.add_message(req, messages.ERROR, "Wrong Credentials!")
        return redirect("Login")

    login(req, user)
    messages.add_message(req, messages.INFO, "Login successful!")
    return redirect("Dashboard")



def logout_view(req):
    logout(req)
    messages.add_message(req, messages.SUCCESS, "Logout successful!")
    return redirect("Login")


def signup(req):
    if req.method == "POST":
        cred = req.POST
        username = cred.get("username", "")
        password = cred.get("password", "")
        confirm = cred.get("confirm_password", "")
        email = cred.get("email", "")
        if User.objects.filter(username=username):
            messages.add_message(req, messages.INFO, "This username already exists!")
            return redirect("Signup")
        if password != confirm:
            messages.add_message(req, messages.ERROR, "Password does not match!")
            return redirect("Signup")
        if not bool(
            re.search(
                r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*()_+[\]{};":|,.<>?])',
                password,
            )
        ):
            messages.add_message(
                req,
                messages.WARNING,
                "Password must include a number, special charecter, upper & lower case!",
            )
            return redirect("Signup")
        otp = random.randint(1000, 9999)
        send_mail(
            "OTP Verification", f"Your OTP is {otp}", settings.EMAIL_HOST_USER, [email]
        )
        req.session["otp"] = otp
        req.session["username"] = username
        req.session["password"] = password
        messages.add_message(req, messages.SUCCESS, "OTP sent at your email!")
        return redirect("Otp")
    return render(req, "signup.html")


def otp(req):
    if req.method == "GET":
        return render(req, "otp.html")
    if req.session.get("otp", "") != int(req.POST.get("otp", "")):
        messages.add_message(req, messages.ERROR, "Wrong OTP!")
        return redirect("Otp")
    user = User.objects.create_user(username=req.session.get("username", ""))
    user.set_password(req.session.get("password", ""))
    user.save()
    messages.add_message(req, messages.SUCCESS, "Successfuly Signed Up")
    return redirect("Login")


@login_required
def dashboard(req):
    if req.user.is_authenticated:
        return render(req, "index.html")
    return render(req, "index.html")


def index(req):

    return redirect("Dashboard")
