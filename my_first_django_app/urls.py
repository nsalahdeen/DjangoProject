from django.urls import path

from . import views

urlpatterns = [
    path("home", views.home_view,name="home_view") #View will be from this url http://127.0.0.1:8000/home
    #path(" ", views.home,name="home.html") #View will be from this url http://127.0.0.1:8000/

]