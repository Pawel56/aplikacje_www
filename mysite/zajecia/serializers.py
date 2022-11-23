from rest_framework import serializers
from .models import Person, Team, Miesiace
import datetime

class PersonSerializer(serializers.Serializer):
    imie = serializers.CharField(required=True)
    nazwisko = serializers.CharField(required=True)
    miesiac_urodzenia = serializers.ChoiceField(choices=Miesiace)
    data_dodania = serializers.DateField()
    druzyna = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all(), allow_null=True)

    def create(self, validated_data):
        return Person.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.imie = validated_data.get('imie', instance.imie)
        instance.nazwisko = validated_data.get('nazwisko', instance.nazwisko)
        instance.miesiac_urodzenia = validated_data.get('miesiac_urodzenia', instance.miesiac_urodzenia)
        instance.save()
        return instance



    def validate(self, data):
        if data['data_dodania'] > datetime.date.today():
            raise serializers.ValidationError("data dodania jest z przyszłości")
        if not data['imie'].isalpha():
            raise serializers.ValidationError("imie zawiera nie tylko litery")
        return data

class PersonModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'name', 'miesiac_dodania', 'data_dodania', 'druzyna']
        read_only_fields = ['id']

class TeamSerializer(serializers.Serializer):
    nazwa = serializers.CharField(required=True)
    kraj = serializers.CharField(required=True)

    def create(self, validated_data):
        return Team.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nazwa = validated_data.get('nazwa', instance.nazwa)
        instance.kraj = validated_data.get('kraj', instance.kraj)
        instance.save()
        return instance

class TeamModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'nazwa', 'kraj']
        read_only_fields = ['id']
