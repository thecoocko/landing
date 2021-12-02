from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
import json


class IndexView (View):
    def get(self,request,*args, **kwargs):
        return render(request, template_name='index.html')


