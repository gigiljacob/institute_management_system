from django.urls import path

from bio.views import Home, Resume, ContactView


app_name = 'profile'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('resume/', Resume.as_view(), name='resume')
]