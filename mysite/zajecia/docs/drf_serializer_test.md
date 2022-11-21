# model Person
from zajecia.models import Person
from zajecia.serializers import PersonSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

person = Person(imie='Adam', nazwisko='Something', miesiac_urodzenia=5)
person.save()

serializer = PersonSerializer(person)
serializer.data

content = JSONRenderer().render(serializer.data)
content

import io

stream = io.BytesIO(content)
data = JSONParser().parse(stream)

deserializer = PersonSerializer(data=data)

deserializer.is_valid()

deserializer.errors

deserializer.validated_data

deserializer.save()

deserializer.data

# model Team

from zajecia.models import Team
from zajecia.serializers import TeamSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

team = Team(nazwa = 'pierogi', kraj = 'PL')
team.save()

serializer = TeamSerializer(team)
serializer.data

content = JSONRenderer().render(serializer.data)
content

import io

stream = io.BytesIO(content)
data = JSONParser().parse(stream)

deserializer = TeamSerializer(data=data)

deserializer.is_valid()

deserializer.errors

deserializer.validated_data

deserializer.save()

deserializer.data