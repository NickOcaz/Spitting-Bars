from django.contrib import admin
from .models import Lyric
#from .models import PostApproval
from .models import Lyric, Genre


# Register your models here.

class LyricAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'genre', 'status', 'admin_accept', 'updated_at')
    search_fields = ('title', 'lyric')
    list_filter = ('status', 'updated_at')
    actions = ['publish_lyrics', 'unpublish_lyrics']
    ordering = ['-status', 'admin_accept', '-updated_at']  # Sort by status (1 first), then by admin_accept (0 first), then by title
    
    def publish_lyrics(self, request, queryset):
        queryset.update(admin_accept=2)  # Set admin_accept to 1 (approved)
        self.message_user(request, "Selected lyrics have been published.")

    def unpublish_lyrics(self, request, queryset):
        queryset.update(admin_accept=0)  # Set admin_accept to 0 (unapproved)
        self.message_user(request, "Selected lyrics have been unpublished.")

    publish_lyrics.short_description = "Accept"
    unpublish_lyrics.short_description = "Deny"

admin.site.register(Lyric, LyricAdmin)
admin.site.register(Genre)
