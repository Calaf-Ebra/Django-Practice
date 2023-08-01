from django.urls import path,include 
from django.contrib import admin
from API import views 
from . import views

urlpattern = [

    path('admin/',admin.site.urls)
    
              ]