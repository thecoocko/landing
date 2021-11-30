from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from ..models import User
from .serializers import UserSerializer


@api_view(['GET','POST'])
class UserView(APIView):
    def create_user(self,request):
        if request.method == 'GET':
            return 1
        elif request.method == 'POST':
            serializer = UserSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)

    
    


class TestApiView(APIView):
    def get(self,request, *args, **kwargs):
        data = [{'id':1,'name':'sanya'}]
        return Response(data)