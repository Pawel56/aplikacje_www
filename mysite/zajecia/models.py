from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

# Create your models here.
class Team(models.Model):
   nazwa = models.CharField(max_length=200)
   kraj = models.CharField(max_length=2)

   def __str__(self):
       return str(self.nazwa + " (" + self.kraj + ")")

class Miesiace(models.IntegerChoices):
    Styczen = 1
    Luty = 2
    Marzec = 3
    Kwiecien = 4
    Maj = 5
    Czerwiec = 6
    Lipiec = 7
    Sierpien = 8
    Wrzesien = 9
    Pazdziernik = 10
    Listopad = 11
    Grudzien = 12

class Person(models.Model):


    imie = models.CharField(max_length=200)
    nazwisko = models.CharField(max_length=200)
    miesiac_urodzenia = models.IntegerField(choices=Miesiace.choices, default=0)
    data_dodania = models.DateField(auto_now_add=True)
    druzyna = models.ForeignKey(Team, default=None, on_delete=models.SET_DEFAULT, null=True, blank=True)
    owner = models.ForeignKey('auth.User', related_name='persons', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.imie+" "+self.nazwisko)

    class Meta:
        managed = True
        db_table = 'person'
        ordering = ["nazwisko"]

