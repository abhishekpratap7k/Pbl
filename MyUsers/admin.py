from django.contrib import admin
from .models import My_User


# Register your models here.


class My_User_admin(admin.ModelAdmin):
    list_display = ["username", "password", "created_date"]
    list_display_links = ["username"]


admin.site.register(My_User,My_User_admin)
