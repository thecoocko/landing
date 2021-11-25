from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.enums import Choices

# Create your models here.
class Language(models.Model):
    LANGUAGE_CHOICES = [
        ('ru', 'Русский'),
        ('en', 'English'),
        ('ua', 'Український'),
    ]
class User(models.Model):
    DEFAULT = 'Выбрать дату'
    FIRST = '01'
    SECOND = '02'
    THIRD = '03'
    language = models.ForeignKey(Language, on_delete=CASCADE, default='ru')
    email =  models.EmailField(("E-mail"), max_length=254, unique= True)
    user_name = models.CharField(("Имя"),max_length=60)
    phone_number = models.CharField(("Телефон"),max_length=60, unique= True)
    DATE_OF_MEETING = [
       (DEFAULT,'Выбрать дату'),
       (FIRST,'01-01-2001'),
       (SECOND,'02-02-2002'),
       (THIRD,'03-03-2003'),
    ]
    date_of_meeting = models.CharField(max_length=50,choices = DATE_OF_MEETING,default = DEFAULT)
   
   
   
    def __str__(self):
       return "%s %s" % (self.user_name, self.email)

