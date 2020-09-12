from django.contrib import admin

from .models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    fields = (
        "title",
        "genre",
        "year",
        "created",
        "modified",
    )
    list_display = (
        "title",
        "slug",
        "genre",
        "year",
        "created",
        "modified",
    )
    readonly_fields = (
        "created",
        "modified",
    )
