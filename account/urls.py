from django.urls import path
from account.views import RegisterView,ShopLoginView,ChangePasswordView,login, register,logout,user_profile


urlpatterns = [
    path('login/',ShopLoginView.as_view(),name="login"),
    path('register/', RegisterView.as_view(), name='register'),
    path('password-change/', ChangePasswordView.as_view(), name='password_change'),
    path('logout/', logout, name='logout'),
    path('profile/', user_profile, name='user_profile'),

]