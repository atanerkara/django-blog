from django.contrib import admin
from .models import Post

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'publishing_Date', 'is_disabled']
    list_display_links = ['title', 'publishing_Date']
    list_filter = ['publishing_Date']
    search_fields = ['title', 'content']
    list_editable = ['is_disabled']

    class Meta:
        model = Post


admin.site.register(Post, PostAdmin)
