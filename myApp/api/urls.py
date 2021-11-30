from django.urls import path
from .views import  UserView


urlpatterns = [
    path('index/', UserView.as_view(), name = 'index')
]
