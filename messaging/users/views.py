from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic


# Create your views here.

from .forms import CustomerUserCreationForm

class SignUp(generic.CreateView):
	form_class = CustomerUserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'signup.html'