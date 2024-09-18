from django.contrib import admin

# Register your models here.
from .models import Post, Category, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "parent",
        "is_visible",
        "position",
    )
    list_filter = ("is_visible",)
    search_fields = ("title",)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "get_category",
        "author",
        "publish",
        "created",
        "updated",
        "status",
    )
    list_filter = (
        "author",
        "publish",
        "status",
    )
    search_fields = ("title", "body")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("name", "body", "post", "created_on", "active")
    list_filter = ("active", "created_on")
    search_fields = ("name", "email", "body")
    actions = ["approve_comments"]

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
