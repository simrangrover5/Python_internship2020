from django.urls import path
from . import views

urlpatterns = [
    path("",views.index),
    path("home/",views.home),
    path("signin/",views.signin),
    path("afterlogin/",views.afterlogin),
    path("register/",views.register),#by default search function for that name so write as_view for the class
    #"" --> localhost/user
    path("aftersignup/",views.aftersignup.as_view()),
    path("logout/",views.logout),
    path("profile/",views.profile),
    path("forgot/",views.forgot),
    path("getemail/",views.getemail),
    path("getotp/",views.getotp),
]