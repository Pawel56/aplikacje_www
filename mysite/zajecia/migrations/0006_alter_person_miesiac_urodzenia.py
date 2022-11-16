# Generated by Django 4.1.2 on 2022-11-03 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zajecia', '0005_person_miesiac_urodzenia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='miesiac_urodzenia',
            field=models.CharField(choices=[('1', 'Styczeń'), ('2', 'Luty'), ('3', 'Marzec'), ('4', 'Kwiecień'), ('5', 'Maj'), ('6', 'Czerwiec'), ('7', 'Lipiec'), ('8', 'Sierpień'), ('9', 'Wrzesień'), ('10', 'Październik'), ('11', 'Listopad'), ('12', 'Grudzień')], default=0, max_length=11),
        ),
    ]
