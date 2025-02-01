from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Personal"), (1, "Published"))
STYLE = ((0, "Rap"), (1, "Song"), (2, "Poem"), (3, "Other"))

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
    style = models.IntegerField(choices=STYLE, default=0)  
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE) #not required style shoiuld be enough
    status = models.IntegerField(choices=STATUS, default=0)
    is_protected = models.BooleanField(default=False) #not neccessary ad the user as a second option to protect with prompt
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["-created_at"]
    
    def __str__(self):
        return self.title

