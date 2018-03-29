from django.shortcuts import render

# Create your views here.
from django.urls import path

from . import views

urlpatterns = [
 path('',views.HomePageView.as_view(),name='home'),
]
