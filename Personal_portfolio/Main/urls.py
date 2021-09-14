from django.contrib import admin
from django.urls import path
from Main.views import home

urlpatterns =[
    path('', home, name="HOME"),
]