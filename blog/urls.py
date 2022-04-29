from django.urls import path
from blog.views import BlogDetailView, BlogListView


urlpatterns = [
    path('blog-list/', BlogListView.as_view(), name='blog_list'),
    path('blog-detail/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
]