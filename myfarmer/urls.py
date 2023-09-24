from django.urls import path
from . import views

urlpatterns = [
    path('',views.index , name="index"),
    path('login',views.login,name="login"),
    path('dologin',views.dologin, name="dologin"),
    path('signup',views.signup, name="signup"),
    path('sign',views.signupFarmer, name="sign"),
    path('farmerhome',views.farmerhome, name="farmerhome"),
    path("videocall/", views.videocall),
    path("book/", views.book),

    
]
