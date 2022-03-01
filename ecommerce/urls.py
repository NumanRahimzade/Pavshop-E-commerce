"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import home, about, contact
from blog.views import blog_list
from blog.views import blog_detail
from order.views import checkout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name=''),
    path('about/', about, name='about'),
    path('blog-list/', blog_list, name='blog_list'),
    path('blog-detail/', blog_detail, name='blog_detail'),
    path('contact/', contact, name='contact'),
    path('checkout/', checkout, name='checkout'),
]
