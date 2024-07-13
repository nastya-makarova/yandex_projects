from django.contrib import admin
from django.contrib.auth.models import Group

from .constants import INLINE_EXTRA_FORMS
from .models import Category, Location, Post


admin.site.empty_value_display = 'Не задано'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'text',
        'pub_date',
        'author',
        'location',
        'category',
        'is_published',
        'created_at'
    )

    list_editable = (
        'is_published',
        'category'
    )

    search_fields = ('title', 'category', 'author', 'location')
    list_filter = ('category', 'author', 'location', 'pub_date')
    list_display_links = ('title',)


class PostInLine(admin.StackedInline):
    model = Post
    extra = INLINE_EXTRA_FORMS


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    inlines = (
        PostInLine,
    )
    list_display = (
        'name',
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        PostInLine,
    )
    list_display = (
        'title',
    )


admin.site.unregister(Group)
