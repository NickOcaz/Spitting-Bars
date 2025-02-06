from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Genre, Lyric
from django.contrib import messages
from django.shortcuts import redirect
from .forms import LyricForm
from django.contrib.auth.decorators import login_required


# Create your views here.

class GenreList(generic.ListView): # Do we need a class? can we just filter via style? 
    queryset = Genre.objects.all()
    template_name = 'lyric_app/genre_list.html'
    

class LyricList(generic.ListView): # if on home page then needs to be only those that are approved by admin
    queryset = Lyric.objects.filter(status=1)
    template_name = 'lyric_app/lyric_list.html'
    context_object_name = 'lyrics'
    paginate_by = 8
    
def home(request):
    return render(request, 'lyric_app/index.html')
    
def lyric_detail(request, pk):
    lyric = Lyric.objects.get(pk=pk)

    return render(request, 'lyric_app/lyric_detail.html', {'lyric': lyric})

@login_required
def lyric_create(request):
    if request.method == 'POST':
        lyricform = LyricForm(request.POST)
        if lyricform.is_valid():
            try:
                lyric = lyricform.save(commit=False)
                lyric.artist = request.user  # Set the artist before saving
                # Ensure admin_accept is set as an integer
                lyric.admin_accept = 1 if lyricform.cleaned_data.get('admin_accept', False) else 0
                lyric.save()
                messages.success(request, 'Lyric created successfully')
                return redirect('home')
            except Exception as e:
                print(f"Error saving lyric: {e}")
                messages.error(request, 'There was an error saving your lyric. Please try again.')
        else:
            print(f"Form errors: {lyricform.errors}")
            messages.error(request, 'There was an error with your submission. Please correct the errors and try again.')
    else:
        lyricform = LyricForm()
    
    return render(request, 'lyric_app/lyric_create.html', {'lyricform': lyricform})

def lyric_edit(request, pk):
    lyric = Lyric.objects.get(pk=pk)
    lyricform = LyricForm(instance=lyric)
    if request.method == 'POST':
        lyricform = LyricForm(request.POST, instance=lyric)
        if lyricform.is_valid():
            lyric = lyricform.save(commit=False)
            lyric.artist = request.user
            lyric.save()
            messages.success(request, 'Lyric updated successfully')
            return redirect('home')
    lyricform = LyricForm(instance=lyric)
    
    return render(request, 'lyric_app/lyric_edit.html', {'lyricform': lyricform, 'lyric': lyric})

def lyric_delete(request, pk):
    lyric = Lyric.objects.get(pk=pk)
    lyric.delete()
    messages.success(request, 'Lyric deleted successfully')
    return redirect('user_page')


def lyric_detail(request, pk):
    lyric = Lyric.objects.get(pk=pk)

    return render(request, 'lyric_app/lyric_detail.html', {'lyric': lyric})

@login_required
def user_page(request):
    user_lyrics = Lyric.objects.filter(artist=request.user)

    return render(request, 'lyric_app/user_page.html', {'lyrics': user_lyrics})
