from django.urls import path
from .views import list_blogs, blog_detail

urlpatterns = [
    path('blogs/', list_blogs, name='blog-list'),
    path('blogs/<int:pk>/', blog_detail, name='blog-detail'),
]
