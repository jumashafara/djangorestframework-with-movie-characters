from django.contrib import admin
from .models import Character
from .models import Movie

# Register your models here.
admin.site.register(model_or_iterable=[Character, Movie])