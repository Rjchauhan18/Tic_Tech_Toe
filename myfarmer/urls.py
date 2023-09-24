from django.urls import path
from . import views

urlpatterns = [
    path('',views.index , name="index"),
    #about us  section
    path('about/',views.about , name="about"),
    path('faq/',views.faq , name="faq"),

    # farmer section paths
    path('pesticides/',views.pesticides,name="pesticides"),
    path('cluster/',views.cluster,name="cluster"),
    path('cultivation/',views.cultivation,name="cultivation"),
    
    path('login',views.login,name="login"),
    path('dologin',views.dologin, name="dologin"),
    path('signup',views.signup, name="signup"),
    path('sign',views.signupFarmer, name="sign"),
    path('farmerhome',views.farmerhome, name="farmerhome"),
    path("book/videocall/", views.videocall),
    path("book/", views.book),

    
]
