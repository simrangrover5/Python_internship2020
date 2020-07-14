from django.urls import path
from . import views

urlpatterns = [
        path("",views.index), #"" --> localhost
        path("login/",views.login)
    ]
