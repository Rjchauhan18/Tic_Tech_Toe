from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from myfarmer.models import *
from myfarmer.EmailBackEnd import EmailBackEnd
from pandas import read_csv
# Create your views here.

def index(request):
    city=request.GET.get('city')
    if city!=None:
        return redirect("book.html", city=city)
    else:
        data =  read_csv('static/MOCK_DATA.csv')
        data = data.to_dict()
        Name=[x for x in data['Name'].values()]
        age=[x for x in data['age'].values()]
        email=[x for x in data['email'].values()]
        City=[x for x in data['City'].values()]
        Experience=[x for x in data['Experience'].values()]
        d={}
        for i in range(len(Name)):
            info = {"age":age[i] ,"Email" :email[i], "City" :City[i], "Experience":Experience[i]}
            d.update({Name[i] : info})
    
    
        return render(request, "index.html",{"data": d })

def book(request):
    return render(request, "book.html")


#about us section 
def about(request):
    return render(request, "aboutus.html")

def faq(request):
    return render(request, "faq.html")


# farmer section
def pesticides(request):
    return render(request, "banned_pesticides.html")


def cluster(request):
    return render(request, "clusterdata.html")

def cultivation(request):
    return render(request, "cultivation_practice.html")

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
        

def videocall(request):
    return render(request,'videocall.html')

def signupFarmer(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password1')
        
        if password == password2:
            new_user = customuser.objects.create(
                                           username=email,
                                           password=password)
            
            new_user.save()
            
            messages.success(request, "user Are succesfully added!")
            return redirect('farmerhome')
        else:
            messages.success(request,"password doesnt match")
            return redirect('')
        
    else:
        messages.success(request,"enter all details")
        return redirect('signup')

def signup(request):
    return render(request, 'signup.html')

def farmerhome(request):
    data =  read_csv('static/MOCK_DATA.csv')
    data = data.to_dict()
    Name=[x for x in data['Name'].values()]
    age=[x for x in data['age'].values()]
    email=[x for x in data['email'].values()]
    City=[x for x in data['City'].values()]
    Experience=[x for x in data['Experience'].values()]
    d={}
    for i in range(len(Name)):
        info = {"age":age[i] ,"Email" :email[i], "City" :City[i], "Experience":Experience[i]}
        d.update({Name[i] : info})
    
    return render(request,'farmerhome.html',{"data": d })