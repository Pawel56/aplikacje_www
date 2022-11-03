from datetime import date

from django.db import models


# Create your models here.
class person(models.Model):
    MIESIACE = (
        ('1', 'Styczeń'),
        ('2', 'Luty'),
        ('3', 'Marzec'),
        ('4', 'Kwiecień'),
        ('5', 'Maj'),
        ('6', 'Czerwiec'),
        ('7', 'Lipiec'),
        ('8', 'Sierpień'),
        ('9', 'Wrzesień'),
        ('10', 'Październik'),
        ('11', 'Listopad'),
        ('12', 'Grudzień'),
    )
    imie = models.CharField(max_length=200)
    nazwisko = models.CharField(max_length=200)
    miesiac_urodzenia = models.CharField(max_length=11, choices=MIESIACE, default=0)
    data_dodania = models.DateField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'person'
