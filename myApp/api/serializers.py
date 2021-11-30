from rest_framework import serializers
from ..models import *


class UserSerializer(serializers.ModelSerializer):
    lang = serializers.ChoiceField(choices=LANGUAGE_CHOICES,required = True)
    email = serializers.EmailField(required = True)
    user_name = serializers.CharField(required = True)
    phone_number = serializers.CharField(required = True)
    date_of_meeting = serializers.ChoiceField(choices=DATE_OF_MEETING,required = True)
    class Meta:
        model = User
        fields = '__all__'

