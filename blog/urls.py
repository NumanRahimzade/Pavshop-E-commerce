from django.urls import path
from blog.views import BlogDetailView, BlogListView, CreateBlogView, UpdateBlogView


urlpatterns = [
    path('blog-list/', BlogListView.as_view(), name='blog_list'),
    path('blog-detail/<slug:slug>/', BlogDetailView.as_view(), name='blog_detail'),
    path('create-blog/', CreateBlogView.as_view(), name='create_blog'),
    path('update-blog/<int:pk>/', UpdateBlogView.as_view(), name='update_blog'),
]