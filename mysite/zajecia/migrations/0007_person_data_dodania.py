# Generated by Django 4.1.2 on 2022-11-03 14:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('zajecia', '0006_alter_person_miesiac_urodzenia'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='data_dodania',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
