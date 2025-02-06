from django.db import models
from django.contrib.auth.models import User


STATUS = ((0, "Personal"), (1, "Publish Me (needs admin approval)"))
STYLE = (("Rap", "Rap"), ("Song", "Song"), ("Poem", "Poem"), ("Other", "Other"))
ADMIN_ACCEPT = ((0, "Private"), (1, "Awaiting Approval"), (2, "Published"))


class Genre(models.Model):
    name = models.CharField(max_length=150, choices=STYLE, default="Rap")
    
    def __str__(self):
        return self.name

class Lyric(models.Model):
    title = models.CharField(max_length=150)
    artist = models.ForeignKey(User, on_delete=models.CASCADE)
    lyric = models.TextField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS, default=0)
    admin_accept = models.IntegerField(choices=ADMIN_ACCEPT, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["-created_at"]
    
    def __str__(self):
        return self.title

      


