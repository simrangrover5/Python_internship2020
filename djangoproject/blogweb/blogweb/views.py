from django.http import HttpResponse


def index(request):
    return HttpResponse("My django project <a href='/user/'>USERS</a>")

def home(request):
    return HttpResponse("<h1 style='color:coral'>Welcome to my home</h1>")

#make variable path --> localhost/simran/80 --> return grade --> B+
#name can be anything and marks can be anything