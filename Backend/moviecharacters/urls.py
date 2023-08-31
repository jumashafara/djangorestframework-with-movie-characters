from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views
app_name = 'moviecharacters'

urlpatterns = [
    path('', views.index, name='index'),
    path('character/<int:id>', views.getSingleCharacter, name='character'),
    path('characters/<int:id>', views.getCharacters, name='characters'),
]
