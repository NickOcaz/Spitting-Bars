from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Genre, Lyric

# Create your views here.

class GenreList(generic.ListView):
    queryset = Genre.objects.all()
    template_name = 'lyric_app/genre_list.html'
    

class LyricList(generic.ListView):
    model = Lyric
    template_name = 'lyric_app/lyric_list.html'
    
def lyric_detail(request, pk):
    lyric = Lyric.objects.get(pk=pk)
    return render(request, 'lyric_app/lyric_detail.html', {'lyric': lyric})