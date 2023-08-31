from .models import Movie, Character
from rest_framework import serializers

# Serializers
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'year']
        
        
class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ['id', 'name', 'age', 'first_appearance']
