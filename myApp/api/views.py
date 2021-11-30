from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import User
from .serializers import UserSerializer
from django.forms import modelform_factory
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core.mail import send_mail


@method_decorator(csrf_exempt, name='dispatch')
class UserView(APIView):
    
    def post(self,request,*args, **kwargs):
        if request.method == 'POST':
            form = modelform_factory(User)
            response = form(request)
            if response.is_valid():
                response.save()
                try:
                    send_mail("User was created","Message success","krabik4794@gmail.com",["cihaw55124@slvlog.com"])
                except Exception:
                    print('Email did not send')
                return Response(status=status.HTTP_201_CREATED)
            else:
               return JsonResponse(response.errors, status=status.HTTP_400_BAD_REQUEST)
    
