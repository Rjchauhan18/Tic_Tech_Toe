from django.shortcuts import render
from app.models import user

# Create your views here.
def login(request):
    return render(request, 'login.html')
    
def home(request):
    Password = request.POST['password']
    Emaill = request.POST['email']
    
    USer = user.objects.create(email = Emaill,password = Password)
    USer.save()
    return render(request, 'home.html')