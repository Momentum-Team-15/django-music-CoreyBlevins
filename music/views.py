from django.shortcuts import render
from django.views.generic import ListView
from .models import Album

# Create your views here.
def index(request):
    albums = Album.objects.all()
    return render(request, 'music/index.html', {'albums': albums})

def album_detail(request, pk):
    album = Album.objects.get(pk=pk)
    return render(request, 'music/album_detail.html', {'album': album})

class HomePageView(ListView):
    model = Album
    template_name = "base.html"
