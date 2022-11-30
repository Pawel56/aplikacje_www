# Generated by Django 4.1.2 on 2022-11-09 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('zajecia', '0011_delete_person_delete_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=200)),
                ('kraj', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=200)),
                ('nazwisko', models.CharField(max_length=200)),
                ('miesiac_urodzenia', models.IntegerField(choices=[(1, 'Styczen'), (2, 'Luty'), (3, 'Marzec'), (4, 'Kwiecien'), (5, 'Maj'), (6, 'Czerwiec'), (7, 'Lipiec'), (8, 'Sierpien'), (9, 'Wrzesien'), (10, 'Pazdziernik'), (11, 'Listopad'), (12, 'Grudzien')], default=0)),
                ('data_dodania', models.DateField(auto_now_add=True)),
                ('druzyna', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='zajecia.team')),
            ],
            options={
                'db_table': 'person',
                'ordering': ['nazwisko'],
                'managed': True,
            },
        ),
    ]