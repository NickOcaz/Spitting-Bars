from .models import Lyric
from django import forms

class LyricForm(forms.ModelForm):
    class Meta:
        model = Lyric
        fields = ['title', 'artist', 'lyric', 'genre', 'status']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'artist': forms.Select(attrs={'class': 'form-control'}),
            'lyric': forms.Textarea(attrs={'class': 'form-control'}),
            'genre': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }