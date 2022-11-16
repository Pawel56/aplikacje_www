from zajecia.models import Person, Team
Person.objects.all()
Person.objects.filter(id = 3)
Person.objects.filter(imie__startswith='b')


