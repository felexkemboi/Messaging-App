from django.urls import path
from . import views

urlpatterns = [
  path('', views.PostListView.as_view(),name='post_list'),
  path('<int:pk>/edit/',views.PostUpdateView.as_view(), name = 'post_edit')
  path('<int:pk>/delete/',views.DeleteView.as_view(),   name = 'post_delete')
  path('<int:pk>/',views.PostDetailView.as_view() ,     name = 'post_detail')
]