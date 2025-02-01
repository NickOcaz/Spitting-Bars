from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User


STATUS = ((0, "Personal"), (1, "Published"))

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
    is_protected = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["-created_at"]
    
    def clean(self):
        if not self.title:
            raise ValidationError('Title cannot be empty')
        if len(self.title) > 150:
            raise ValidationError('Title is too long')
        if not self.lyric:
            raise ValidationError('Lyric content cannot be empty')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title


class PostApproval(models.Model):
    lyric = models.OneToOneField(Lyric, on_delete=models.CASCADE)
    approved_by = models.ForeignKey(User, on_delete=models.CASCADE)
    approved_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    
    def __str__(self):
        return f"{self.lyric.title} - {'Published' if self.status == 1 else 'Draft'}"