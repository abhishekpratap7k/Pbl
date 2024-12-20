"""
URL configuration for PBL project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path("", views.index, name="index"),
    path("Dashboard", views.dashboard, name="Dashboard"),
    path("Login", views.login_view, name="Login"),
    path("Logout", views.logout_view, name="Logout"),
    path("SignUp", views.signup, name="Signup"),
    path("OTP", views.otp, name="Otp"),
    path("ForgotPassword", views.forgot_pass, name="forgot_pass"),
    path("ForgotPasswordOTP", views.forgot_pass_opt, name="forgot_pass_opt"),
    path("NewPassword", views.password_change, name="password_change"),
    path("__reload__", include("django_browser_reload.urls")),
]

admin.site.site_title="PBL"
admin.site.site_header="PBL Admin Page"
admin.site.index_title="Available Data Tables"