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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns



urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n")),
    path("api/", include('product.api.urls')),
    path("api/account/", include('account.api.urls')),
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    path('admin/', admin.site.urls),
    path('', include('social_django.urls', namespace='social')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "PAVSHOP Admin"
admin.site.site_title = "PAVSHOP Admin Portal"
admin.site.index_title = "Welcome to PAVSHOP Portal"

urlpatterns += i18n_patterns(
    path('', include('core.urls')),
    path('', include('blog.urls')),
    path('', include('product.urls')),
    path('', include('account.urls')),
    path('', include('order.urls')),
) 