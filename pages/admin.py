from django.contrib import admin

from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "author",
        "photo",
        "title",
        "preview_text",
        "is_published",
        "publish_date",
        "creation_date",
        "last_modified",
    )
    list_display_links = (
        "id",
        "author",
        "title",
    )
    list_editable = ("is_published",)
    search_fields = (
        "author",
        "title",
        "preview_text",
    )
    list_per_page = 20
    list_filter = (
        "author",
        "publish_date",
        "last_modified",
    )


admin.site.register(Post, PostAdmin)