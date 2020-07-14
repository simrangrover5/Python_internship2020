from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .forms import Login

def index(request):
    return render(request,"index.html")  #the page specified here is find on those directories 
#that you have configured in your settings.py file
#here the html page will be found in myproject/templates/index.html
    #return HttpResponse("Welcome again to my app i knew that you won't understand django at first")


def login(request):
    form = Login()  #object of login class
    return render(request,"login.html",{'form':form})
