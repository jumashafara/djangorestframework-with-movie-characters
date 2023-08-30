from .models import Movie
from .models import Character
from django.shortcuts import render
from django.core.paginator import Paginator

# Create your views here.
from django.shortcuts import render

def index(request):
    movies = Movie.objects.all()
    print(movies)
    context = {'movies': movies}
    return render(request, template_name='moviecharacters/index.html', context=context)


def getCharacters(request, id):
    characters = Character.objects.filter(movie=id)
    paginator = Paginator(characters, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'characters': page_obj, 'movie':'Rick and Morty'}
    return render(request, 'moviecharacters/characters.html', context=context)