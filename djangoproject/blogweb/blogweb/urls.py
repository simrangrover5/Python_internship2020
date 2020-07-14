"""blogweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views  #. --> pwd , views.py (import)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index), #"" --> domain --> localhost
    path("home/",views.home), #localhost/home/ --> views.home
    path("user/",include('users.urls')),
    path("blog/",include("blog.urls")), #localhost/blog/ --> blog--> app
    #if anyone write path localhost/user/ and so on then redirect it to users --> urls
    #path(url,func_name)
]
