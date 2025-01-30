from django.contrib import admin
from .models import Lyric


# Register your models here.
class LyricAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'status', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ('status', 'updated_at')

admin.site.register(Lyric)

