from django.contrib import admin
from .models import Lyric, Genre


# Register your models here.

class LyricAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'genre', 'status', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ('status', 'updated_at')
    actions = ['publish_lyrics', 'unpublish_lyrics']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(status=0)  # Assuming 'published' corresponds to 1

    def publish_lyrics(self, request, queryset):
        queryset.update(status=1)  # Assuming 'published' corresponds to 1
        self.message_user(request, "Selected lyrics have been published.")

    def unpublish_lyrics(self, request, queryset):
        queryset.update(status=0)  # Assuming 'unpublished' corresponds to 0
        self.message_user(request, "Selected lyrics have been unpublished.")

    publish_lyrics.short_description = "Accept"
    unpublish_lyrics.short_description = "Deny"

admin.site.register(Lyric, LyricAdmin)

admin.site.register(Genre)

