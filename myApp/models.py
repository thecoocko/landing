from django.db import models


LANGUAGE_CHOICES = [

    ('ru', 'Русский'),
    ('en', 'English'),
    ('ua', 'Українська'),
]

FIRST = '20'
SECOND = '30'
THIRD = '10'
DATE_OF_MEETING = [

    (FIRST,'20-11-2021'),
    (SECOND,'30-11-2021'),
    (THIRD,'10-12-2021'),
]
    
class User(models.Model):
    language = models.CharField(max_length=40,choices=LANGUAGE_CHOICES, default='ru')
    email =  models.EmailField(max_length=254, unique= True)
    user_name = models.CharField(max_length=60)
    phone_number = models.CharField(max_length=60, unique= True)
    date_of_meeting = models.CharField(max_length=50,choices = DATE_OF_MEETING,default = FIRST)
   
    def __str__(self):
       return "%s %s" % (self.user_name, self.email)

class Field(models.Model):
    field_name = models.CharField(max_length=20,unique=True)
    #ru, en, ua
    
