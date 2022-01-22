from turtle import home
from unicodedata import name
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name="home"),
    path("about", views.about, name="about"),
    path("services", views.services, name="services"),
    path("blog", views.blog, name="blog"),
    path("contact", views.contact, name="contact")
]
