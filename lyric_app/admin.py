from django.contrib import admin
from .models import Lyric
from .models import PostApproval




# Register your models here.
class LyricAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'status', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ('status', 'updated_at')

admin.site.register(Lyric)


class PostApprovalAdmin(admin.ModelAdmin):
    list_display = ('get_post_title', 'approved_by', 'approved_at')
    search_fields = ('post__title', 'approved_by__username')
    list_filter = ('approved_at',)

    def get_post_title(self, obj):
        return obj.post.title
    get_post_title.admin_order_field = 'post'  # Allows column order sorting
    get_post_title.short_description = 'Post Title'  # Renames column head

admin.site.register(PostApproval, PostApprovalAdmin)