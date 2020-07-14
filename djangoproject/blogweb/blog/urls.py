from django.urls import path
from . import views


urlpatterns = [
    path("",views.index),
    path("addblog/",views.addblog),
    path("afterblog/",views.afterblog),
    path("allblog/",views.allblog),
    path("myblog/",views.myblog),
    path("topblogs/",views.topblogs),
    path("search/",views.search),
    path("api/",views.api.as_view())
]