from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url 

urlpatterns = [
    url(r'^', include('myApp.urls')),
    #url(r'^index/?'),
    path('admin/', admin.site.urls),
    url(r'^', include('myApp.api.urls')),
    #path('api/',include('myApp.api.urls'))
]
