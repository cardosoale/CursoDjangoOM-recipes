from django.contrib import admin

from .models import Category, Recipe


class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'created_at', 'author', 'is_published',
    list_display_links = 'title',
    search_fields = 'id', 'title', 'description', 'slug', 'preparation_steps',
    list_filter = 'is_published', 'category', 'author', \
        'preparation_steps_is_html',
    list_editable = 'is_published',
    ordering = '-id',
    prepopulated_fields = {
        'slug': ('title',)
    }


admin.site.register(Category, CategoryAdmin)
