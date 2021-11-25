from django.shortcuts import render
from django.views import View

# Create your views here.
# Create your views here.Добавить оповещение о регистрации

def index(req):
    return render(req,template_name='index.html')
