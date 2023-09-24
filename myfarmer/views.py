from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from myfarmer.models import *
from myfarmer.EmailBackEnd import EmailBackEnd
from pandas import read_csv
# Create your views here.

def index(request):
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
    print(d)
    # data={"Name" :Name,"age":age ,"Email" :email, "City" :City, "Experience":Experience}
    # print(Name)
    # for d in data :
    #     for k in data[d]:
    #         print(k)
    # print(data.Name)
        # for d in data:

        #     print(d)
    return render(request, "index.html",{"data": d })

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
        
def signupFarmer(request):
    if request.method == "POST":
        Name = request.POST.get('name')
        

def signup(request):
    return render(request, 'signup.html')

def videocall(request):
    return render(request,'videocall.html')