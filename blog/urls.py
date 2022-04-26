from django.urls import path
from blog.views import blog_list, BlogDetailView


urlpatterns = [
    path('blog-list/', blog_list, name='blog_list'),
    path('blog-detail/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
]