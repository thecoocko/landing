from django.http import JsonResponse
from django.views.generic import View
from ..models import Field, User
from django.forms import  modelform_factory
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core.mail import send_mail


@method_decorator(csrf_exempt, name='dispatch')
class UserViewAPI(View):
    @csrf_exempt
    def post(self,request,*args, **kwargs):
        form = modelform_factory(User, fields='__all__')
        obj = {
            "language": request.POST['language'],
            "email":request.POST['email'],
            "user_name":request.POST['name'],
            "phone_number":request.POST['phone'],
            "date_of_meeting":request.POST['meet'],
        }
        response = form(obj)
        print(obj)
        if response.is_valid():
            response.save()
            try:
                send_mail("User was created","Message success","email",["cihaw55124@slvlog.com"])
            except Exception:
                return 0
            return JsonResponse({'message':[]})
        else:
            return JsonResponse({'error':[response.errors]})

class TranslateViewAPI(View):
    def post(self,request,*args, **kwargs):
        language = request.META['HTTP_ACCEPT_LANGUAGE']
        language = language.split('-')[0]