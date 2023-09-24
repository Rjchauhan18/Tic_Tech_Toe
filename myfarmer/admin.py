from django.contrib import admin
from.models import *
from django.contrib.auth.admin import UserAdmin

#Register your models here.
class usermodel(UserAdmin):
    list_display = ['username','user_type']    
admin.site.register(customuser,usermodel)
admin.site.register(Farmer)