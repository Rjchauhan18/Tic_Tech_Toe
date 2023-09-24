from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from myfarmer.models import *
from myfarmer.EmailBackEnd import EmailBackEnd

# Create your views here.
def index(request):
    return render(request, "index.html")

def book(request):
    return render(request, "book.html")

def login(request):
    return render(request, "login.html")

def dologin(request):
    if request.method == "POST":
        user = EmailBackEnd.authenticate(request,
                                         email=request.POST.get('email'),
                                         password=request.POST.get('password'))
        if user!=None:
            user_type = user.user_type
            if user_type == '1':
                return HttpResponse('Admin')
            elif user_type == '2':
                return HttpResponse('experts')
            elif user_type == '3':
                return HttpResponse('farmer')
            else:
                messages.error(request,'Email and Password Are Invalid !')
                return redirect('login')
        else: 
            messages.error(request,'Email and Password Are Invalid !')
            return redirect('login')

def signup(request):
    return render(request, 'signup.html')

def videocall(request):
    return render(request,'videocall.html')