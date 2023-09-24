from django.urls import path
from . import views

urlpatterns = [
    path('',views.index , name="index"),
    path('login',views.login,name="login"),
    path('dologin',views.dologin, name="dologin"),
    path('signup',views.signup, name="signup"),
    path("videocall/", views.videocall),
    path("book/", views.book),

    
]
