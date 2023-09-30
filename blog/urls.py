from django.urls import path

from blog.views import Home


app_name = 'blog'
urlpatterns = [
    path('', Home.as_view(), name='home')
]