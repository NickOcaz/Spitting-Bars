from django.db import models
from django.contrib.auth.models import User


STATUS = ((0, "Draft"), (1, "Publish"))

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=150)
    excerpt = models.TextField()
    
    def __str__(self):
        return self.name


class Lyric(models.Model):
    title = models.CharField(max_length=150)
    artist = models.ForeignKey(User, on_delete=models.CASCADE)
    lyric = models.TextField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
