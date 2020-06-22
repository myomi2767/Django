from django.shortcuts import render
from .models import Musician, Album

# Create your views here.
def index(request):
    musicians = Musician.objects.all()[::-1]
    context = {
        'musicians' : musicians
    }
    return render(request, 'musicians/index.html', context)

def detail(request, musician_pk):
    albums = Album.objects.filter(musician_id = musician_pk)
    context = {
        'albums' : albums
    }
    return render(request, 'musicians/detail.html', context)
