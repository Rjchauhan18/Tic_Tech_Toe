from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def book(request):
    return render(request, "book.html")

def login(request):
    return render(request, "login.html")

def signup(request):
    return render(request, 'signup.html')

def videocall(request):
    return render(request,'videocall.html')