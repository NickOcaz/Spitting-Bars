from .models import Lyric
from django import forms

class LyricForm(forms.ModelForm):
    class Meta:
        model = Lyric
        fields = ['title', 'lyric', 'style', 'status',] # ['is_protected'] not required
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'lyric': forms.Textarea(attrs={'class': 'form-control'}),

            'style': forms.Select(attrs={'class': 'form-control'}), 
        #    'genre': forms.Select(attrs={'class': 'form-control'}), # not required

            'status': forms.Select(attrs={'class': 'form-control'}),
            'is_protected': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }