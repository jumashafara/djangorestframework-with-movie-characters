# import models
from .models import Movie
from .models import Character
# import django tools
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
# import serializers and rest_framework tools
from .serializers import MovieSerializer
from .serializers import CharacterSerializer
from rest_framework.parsers import JSONParser


# Create your views here.
@csrf_exempt
def index(request):
    """
    get all movies or create a movie
    """
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(instance=movies, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MovieSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
@csrf_exempt
def getCharacters(request, id):
    if request.method == 'GET':
        characters = Character.objects.filter(movie=id)
        serializer = CharacterSerializer(instance=characters, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CharacterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    