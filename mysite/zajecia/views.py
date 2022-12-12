from django.db.models import Q
from django.shortcuts import render
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Person, Team
from .serializers import PersonSerializer, TeamSerializer

@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes((IsAuthenticated,))
def person_detail(request, pk):
    try:
        person = Person.objects.get(pk=pk)
    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        person = Person.objects.get(pk=pk)
        serializer = PersonSerializer(person)
        return Response(serializer.data)

@api_view(['PUT'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
def person_update(request, pk):
    try:
        person = Person.objects.get(pk=pk)
    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes((IsAuthenticated,))
def person_delete(request, pk):
    try:
        person = Person.objects.get(pk=pk)
    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def person_list(request):
    if request.method == 'GET':
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def person_search(request, nazwa):
    if request.method == 'GET':
        persons = Person.objects.filter(imie__contains=nazwa)
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def team_detail(request, pk):

    try:
        team = Team.objects.get(pk=pk)
    except Team.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        team = Team.objects.get(pk=pk)
        serializer = TeamSerializer(team)
        return Response(serializer.data)

@authentication_classes([SessionAuthentication, BasicAuthentication])
@api_view(['PUT'])
def team_update(request, pk):

    try:
        team = Team.objects.get(pk=pk)
    except Team.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = TeamSerializer(team, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def team_delete(request, pk):

    try:
        team = Team.objects.get(pk=pk)
    except Team.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        team.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@authentication_classes([SessionAuthentication, BasicAuthentication])
@api_view(['GET'])
def teams_list(request):
    if request.method == 'GET':
        team = Team.objects.all()
        serializer = TeamSerializer(team, many=True)
        return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
#@permission_classes([IsAuthenticated])
def team_persons_list(request, pk):
    if request.method == 'GET':
        persons = Person.objects.filter(Q(druzyna = pk))
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)