from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User,Group


def login_view(req):
    if req.method == "POST":
        cred= req.POST
        
        username = cred.get("username", "")
        password = cred.get("password", "")

        if User.objects.filter(username=username).exists():
            if user:=authenticate(request=req,username=username,password=password):
                login(req,user)
                # print(user.groups.all().get(0))
                # isAdmin=user.groups.filter(name="Admin").exists()
                # return render(req,'index.html',{"isAdmin":isAdmin})
                return redirect('Dashboard')
        

    return render(req, "login.html")

def logout_view(req):
    logout(req)
    return redirect('Login')


def signup(req):
    if req.method == "POST":
        cred = req.POST
        username = cred.get("username", "")
        password = cred.get("password", "")
        confirm = cred.get("confirm_password", "")
        if password == confirm:
            if not User.objects.filter(username=username):
                user=User.objects.create(username=username)
                group=Group.objects.get(name='Student')
                user.groups.add(group)
                user.set_password(password)
                user.save()
                return redirect("Login")
    return render(req, "signup.html")


def otp(req):
    return render(req, "otp.html")


def dashboard(req):
    
    if req.user.is_authenticated:
        isAdmin = req.user.groups.filter(name="Admin").exists()
        return render(req, "index.html", {"isAdmin": isAdmin})
    return render(req, "index.html")


def index(req):

    return redirect("Dashboard")
