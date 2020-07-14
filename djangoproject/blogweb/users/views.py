from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from django.views import View
from .models import Adduser
from django.core.mail import send_mail
from django.conf import settings  #setting.py
from random import randint
# Create your views here.

def index(request):
    return render(request,"index.html")
    #return HttpResponse("This is my users app")

def home(request):
    return HttpResponse("This is the home page!!!!!!!!!!!")

def signin(request):
    f = Login()
    return render(request,"signin.html",{'form':f})
    #error=error

def afterlogin(request):
    if request.method == "POST":
        form = Login(request.POST)
        if form.is_valid(): #validation --< email -> email, textfield --> text, Imagefield --> image
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                obj = Adduser.objects.get(email=email)
            except Exception as e:
                error = "Does Not Exist Sigup to signin"
                form = Signup()
                return render(request,"signup.html",{'error':error,'form':form})
            else:
                if password == obj.password:
                    request.session['email'] = email
                    request.session['islogin'] = "true"
                    return render(request,"afterlogin.html")
                    #return HttpResponse(f"{email} {password}")
                else:
                    error = "Invalid Password"
                    form = Login()
                    return render(request,"signin.html",{'error':error,'form':form})
        else:
            error = "Invalid form"
            form = Login()
            return render(request,"signin.html",{'error':error,'form':form})
    else:
        if request.session.get("islogin"):
            return render(request,"afterlogin.html")
    


def register(request):
    form = Signup()
    return render(request,"signup.html",{"form":form})

class aftersignup(View):
    def get(self,request):  #for get method request
        form = Signup()
        return render(request,"signup.html",{'form':form})
    
    def post(self,request):  #for post method request
        form = Signup(request.POST,request.FILES)
        if form.is_valid():
            email = form.cleaned_data["email"]
            fname = form.cleaned_data["fname"]
            lname = form.cleaned_data["lname"]
            password = form.cleaned_data["password"]
            image = form.cleaned_data["image"]
            try:
                obj = Adduser.objects.get(email=email)
            except Exception as e:
                Adduser.objects.create(fname=fname,lname=lname,email=email,password=password,image=image)
                error = "Login to Continue..."
                form = Login()
                return render(request,"signin.html",{'error':error,'form':form})
            else:
                error = "Already Registered!!!"
                form = Signup()
                return render(request,"signup.html",{'error':error,'form':form})
            #return HttpResponse(f"{email}")
        else:
            error = "Invalid Form"
            form = Signup()
            return render(request,"signup.html",{'form':form,'error':error})

def logout(request):
    del request.session['email']
    del request.session['islogin']
    return redirect("/user/")

def profile(request):
    user = Adduser.objects.get(email=request.session.get("email"))
    data = {
        "fname" : user.fname,
        "lname" : user.lname,
        "email" : user.email,
        "image" : str(user.image).split("/")[-1]
    }
    print(data["image"]) 
    return render(request,"profile.html",{'data':data})
#database --> mysql or sqlite
#if your use mysql --> mysql server --> database
#put conditions on password 
#encrpt your password --> django --> hashlib
def forgot(request):
    form = Forgot()
    return render(request,"forgotpass.html",{'form':form})

def getemail(request):
    form = Forgot(request.POST)
    if form.is_valid():
        email = form.cleaned_data["email"]
        try:
            Adduser.objects.get(email=email)
        except:
            error = "Invalid Email"
            form = Login()
            return render(request,{'form':form,'error':error})
        else:
            otp = randint(1000,9999)
            subject = "Otp for password change"
            message = f"Thanks for using our services and otp for our password is {otp}"
            to_email = "simrangrover5@gmail.com"
            from_email = "simrangrover5@gmail.com"
            request.session['otp'] = str(otp)
            send_mail(subject=subject,message=message,from_email=from_email,recipient_list=[to_email],auth_password=settings.EMAIL_HOST_PASSWORD)
            form = Otp()
            return render(request,"otp.html",{'form':form})
        
def getotp(request):
    form = Otp(request.POST)
    if form.is_valid():
        otp = form.cleaned_data['otp']
        if otp == request.session.get("otp"):
            del request.session['otp']
        else:
            del request.session['otp']
            error = "Otp does not match!!!"
            form = Login()
            return render(request,"signin.html",{'error':error,'form':form})

#blogapp --> blog form --> title,post,....
# model --> data store 
