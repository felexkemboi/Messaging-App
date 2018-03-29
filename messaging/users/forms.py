from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

	class Meta(UserCreationForm.meta):
		model = CustomUser
		fields = UserCreationForm.meta.fields

class CustomUserChangeForm(UserChangeForm):
	
	class Meta:
		model = CustomUser
		fields = CustomUserChangeForm.Meta.fields

		