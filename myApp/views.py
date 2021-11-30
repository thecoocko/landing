from django.shortcuts import render
from django.views.generic import View
#https://coderoad.ru/57961017/Отправка-данных-из-формы-React-в-Django-Rest-Framework-без-модели

class IndexView (View):
    def get(self,req,*args, **kwargs):
        return render(req, template_name='index.html')


