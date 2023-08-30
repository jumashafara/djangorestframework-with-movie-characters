from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views
app_name = 'moviecharacters'

urlpatterns = [
    path('', views.index, name='index'),
    path('characters<int:id>', views.getCharacters, name='characters'),
]
