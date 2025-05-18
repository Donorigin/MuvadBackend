from django.urls import path
from .views import *

urlpatterns = [
    path('blogs/', list_blogs, name='blog-list'),
    path('blogs/<int:pk>/', blog_detail, name='blog-detail'),
    path('blogs/create/', create_blog),
    path('blogs/<int:pk>/update/', update_blog),
    path('blogs/<int:pk>/delete/', delete_blog),
    path('login/', login_user),
]
