from django.contrib import admin

# Register your models here.

from .models import Person
from .models import Team


class PersonAdmin(admin.ModelAdmin):
    list_display = ['imie', 'nazwisko', 'miesiac_urodzenia', 'data_dodania', 'druzyna']
    list_filter = ('data_dodania', 'druzyna',)

class TeamAdmin(admin.ModelAdmin):
    list_display = ['nazwa', 'kraj']
    list_filter = ('kraj',)

admin.site.register(Person, PersonAdmin)
admin.site.register(Team, TeamAdmin)

