from django.contrib import admin
from django.urls import path,include
from . import views

#settings urls for app (auth)
urlpatterns = [
    path('', views.home, name = 'home'),
    path('signup', views.signup, name="signup"),
    path('signup', views.signup, name="signup"),
    path('signup', views.signup, name="signup"),



]
    
