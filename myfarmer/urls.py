from django.urls import path
from . import views

urlpatterns = [
    path("videocall/", views.videocall)
    
]
