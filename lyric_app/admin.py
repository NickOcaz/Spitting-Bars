from django.contrib import admin
from .models import Lyric


# Register your models here.
class LyricAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ('published', 'updated_at')

admin.site.register(Lyric)

