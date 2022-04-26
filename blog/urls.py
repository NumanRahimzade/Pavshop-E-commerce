from django.urls import path
from blog.views import blog_detail, BlogListView


urlpatterns = [
    
    path('blog-list/', BlogListView.as_view(), name='blog_list'),
    path('blog-detail/<int:id>/', blog_detail, name='blog_detail'),
]