from django.db import models


# Create your models here.
class Team(models.Model):
   nazwa = models.CharField(max_length=200)
   kraj = models.CharField(max_length=2)

   def __str__(self):
       return str(self.nazwa + " (" + self.kraj + ")")

class Person(models.Model):
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

    imie = models.CharField(max_length=200)
    nazwisko = models.CharField(max_length=200)
    miesiac_urodzenia = models.IntegerField(choices=Miesiace.choices, default=0)
    data_dodania = models.DateField(auto_now_add=True)
    druzyna = models.ForeignKey(Team, default=None, on_delete=models.SET_DEFAULT, blank=True)

    def __str__(self):
        return str(self.imie+" "+self.nazwisko)

    class Meta:
        managed = True
        db_table = 'person'
        ordering = ["nazwisko"]

