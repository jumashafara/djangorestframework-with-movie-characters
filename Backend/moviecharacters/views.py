# import models
from .models import Movie
from .models import Character
# import django tools
from django.views.decorators.csrf import csrf_exempt
# import serializers and rest_framework tools
from .serializers import MovieSerializer
from .serializers import CharacterSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.
@api_view(http_method_names=['GET', 'POST'])
def index(request):
    """
    get all movies or create a movie
    """
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(instance=movies, many=True)
        return Response(data=serializer.data)
    
    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(http_method_names=['GET', 'POST'])
def getCharacters(request, id):
    """
    Retrive movies, and send, update or delete
    """
    if request.method == 'GET':
        characters = Character.objects.filter(movie=id)
        serializer = CharacterSerializer(instance=characters, many=True)
        return Response(data=serializer.data)
    
    elif request.method == 'POST':
        serializer = CharacterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(http_method_names=['GET', 'POST', 'PUT', 'DELETE'])
def getSingleCharacter(request, id):
    """
    Retrive character, and send, update or delete
    """
    try:
        character = Character.objects.get(id=id)
    except Character.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    if request.method == 'GET':
        serializer = CharacterSerializer(instance=character)
        return Response(data=serializer.data)
    
    elif request.method == 'POST':
        serializer = CharacterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PUT':
        serializer = CharacterSerializer(instance=character, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        character.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)