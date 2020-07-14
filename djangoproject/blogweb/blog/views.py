from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from .models import Blog
from users.models import Adduser
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BlogSerializers
# Create your views here.

def index(request):
    return HttpResponse("<label style='color:coral;font-size:30px'>This is blog app </label>")


def addblog(request):
    if request.session.get("email"):
        form = Addblog()
        return render(request,"blogform.html",{'form':form})
    else:
        return redirect("/user/signin/")

def afterblog(request):
    if request.method == "POST":
        form = Addblog(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            post = form.cleaned_data['post']
            category = form.cleaned_data['categories']
            author = Adduser.objects.get(email=request.session.get("email"))
            Blog.objects.create(author=author,title=title,post=post,category=category)
            error = "Successfully uploaded the blog"
            return render(request,"afterlogin.html",{'error':error})
        else:
            error = "Invalid Form"
            form = Addblog()
            return render(request,"blogform.html",{'error':error,'form':form})
    else:
        return redirect("/blog/addblog/")

def allblog(request):
    all_data = Blog.objects.all()
    blogs = []
    for i in all_data:
        d = {}
        d['title'] = i.title
        d['post'] = i.post
        d['date'] = i.date 
        d['email'] = i.author.email
        d['category'] = i.category
        blogs.append(d)
    return render(request,"allblogs.html",{'blogs':blogs})

def myblog(request):
    obj = Adduser.objects.get(email = request.session.get("email"))
    #id is pk in user table so give pk as argument in condition
    my = Blog.objects.filter(author=obj.id)
    #my = Blog.objects.filter(author=Adduser.objects.get(request.session.get("email")))
    blogs = []
    for i in my:
        d = {}
        d['title'] = i.title
        d['post'] = i.post
        d['date'] = i.date 
        d['email'] = i.author.email
        d['category'] = i.category
        blogs.append(d)
    return render(request,"allblogs.html",{'blogs':blogs})

def topblogs(request):
    all_data = Blog.objects.all()[:10]
    blogs = []
    for i in all_data:
        d = {}
        d['title'] = i.title
        d['post'] = i.post
        d['date'] = i.date 
        d['email'] = i.author.email
        d['category'] = i.category
        blogs.append(d)
    return render(request,"topblog.html",{'blogs':blogs})

def search(request):
    category = request.POST.get("category")
    all_data = Blog.objects.filter(category=category)
    blogs = []
    for i in all_data:
        d = {}
        d['title'] = i.title
        d['post'] = i.post
        d['date'] = i.date 
        d['email'] = i.author.email
        d['category'] = i.category
        blogs.append(d)
    return render(request,"allblogs.html",{'blogs':blogs})
    #return HttpResponse(f"{category}")
#filter --> form --> education,entertainment
# create own api in django 
# web scraping / regular expression

class api(APIView):
    def get(self,request):  #to handle get method request
        all_data = Blog.objects.all()
        blog = BlogSerializers(all_data,many=True)
        return Response(blog.data)
    
    def post(self,request):
        print(request.data)

    
