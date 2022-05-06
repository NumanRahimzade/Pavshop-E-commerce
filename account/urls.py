from django.urls import path, re_path
from account.views import (RegisterView,ShopLoginView,ChangePasswordView,
            login, register,logout,
            user_profile,
            Activate,
            ResetPasswordView,
            CustomPasswordResetConfirmView, UpdateUserView
)


urlpatterns = [
    path('login/',ShopLoginView.as_view(),name="login"),
    path('register/', RegisterView.as_view(), name='register'),
    path('password-change/', ChangePasswordView.as_view(), name='password_change'),
    path('update-userinfo/<int:pk>', UpdateUserView.as_view(), name='update_user_info'),
    path('logout/', logout, name='logout'),
    path('profile/', user_profile, name='user_profile'),
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,33})/$',
        Activate.as_view(), name='activate'),
    re_path(r'^password-reset-confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,33})/$',
        CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
] 