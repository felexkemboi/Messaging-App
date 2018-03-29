from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.
from . import models

class PostListView(ListView):
	model = models.Post
	template_name = 'post_list.html'
