from django.contrib.auth import views as auth_views
from django.urls import path

from accounts.api_views import ImsRegisterApi, UserDetailAPI, ImsTokenObtainPairView
from accounts.views import UserRegister, ImsLoginView, ImsProfileView, ResetPasswordView

app_name = 'accounts'
api_version = 'v1'


urlpatterns = [
    # Django Urls
    path('register/', UserRegister.as_view(), name='register'),
    path('login/', ImsLoginView.as_view(), name='login'),
    path('profile/', ImsProfileView.as_view(), name='profile'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password-reset/', ResetPasswordView.as_view(), name='change_password'),

    # Django Rest API Urls
    path(f'api/{api_version}/register/', ImsRegisterApi.as_view(), name='register_api'),
    path(f'api/{api_version}/login/', ImsTokenObtainPairView.as_view(), name='login_api'),
]
