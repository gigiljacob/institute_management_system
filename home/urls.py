from django.urls import path

from home.views import HomeView, ContactMe, AboutMe


app_name = 'home'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contact/', ContactMe.as_view(), name='contact'),
    path('about/', AboutMe.as_view(), name='about'),
]