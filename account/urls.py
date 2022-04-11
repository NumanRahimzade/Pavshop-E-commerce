from django.urls import path
from account.views import login, register, user_profile, logout


urlpatterns = [
    path('login/',login,name="login"),
    path('register/',register,name="register"),
    path('logout/', logout, name='logout'),
    path('profile/', user_profile, name='user_profile'),

]