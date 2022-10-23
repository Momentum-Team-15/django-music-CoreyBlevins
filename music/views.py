from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .models import Album
from music.forms import PostForm

def index(request):
    albums = Album.objects.all()
    return render(request, 'music/index.html', {'albums': albums})

def album_detail(request, pk):
    album = Album.objects.get(pk=pk)
    return render(request, 'music/album_detail.html', {'album': album})

def create_album(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = PostForm()
    return render(request, 'music/create_album.html', {'form': form})

def album_edit(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=album)
        if form.is_valid():
            album = form.save()
            return redirect('album_detail', pk=album.pk)
    else:
        form = PostForm(instance=album)
    return render(request, 'music/album_edit.html', {'form': form})

def delete_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == "POST":
        album.delete()
        return redirect("home")
    return render(request, "music/delete_album.html")

class Cover(ListView):
    model = Album
    template_name = "base.html"
