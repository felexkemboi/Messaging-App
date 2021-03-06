from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.
from . import models

class PostListView(ListView):
	model = models.Post
	template_name = 'post_list.html'

class PostDetailView(DetailView):
	model = models.Post
	template_name = 'post_detail.html'

class PostUpdateView(UpdateView):
	model = models.Post
	fields = ['message']
	template_name = 'post_edit.html'

class PostDeleteView(ListView):
	model = models.Post
	template_name = 'post_delete.html'
	success_url = reverse_lazy('post_list')
