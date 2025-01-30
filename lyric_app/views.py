from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Genre, Lyric
from django.contrib import messages
from django.shortcuts import redirect
from .form import LyricForm

# Create your views here.

class GenreList(generic.ListView):
    queryset = Genre.objects.all()
    template_name = 'lyric_app/genre_list.html'
    

class LyricList(generic.ListView):
    queryset = Lyric.objects.all()
    template_name = 'lyric_app/lyric_list.html'
    context_object_name = 'lyrics'
    paginate_by = 8
    
def lyric_detail(request, pk):
    lyric = Lyric.objects.get(pk=pk)

    return render(request, 'lyric_app/lyric_detail.html', {'lyric': lyric})

def lyric_create(request):
    lyricform = LyricForm()
    if request.method == 'POST':
        lyricform = LyricForm(request.POST)
        if lyricform.is_valid():
            lyric = lyricform.save(commit=False)
            lyric.artist = request.user
            lyric.save()
            messages.add_message(request, 'Lyric created successfully')
            return redirect('home')
    lyricform = LyricForm()
    
    return render(request, 'lyric_app/lyric_create.html', {'lyricform': lyricform})