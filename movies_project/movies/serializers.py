from rest_framework import serializers

from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = (
            "id",
            "title",
            "slug",
            "genre",
            "year",
            "created",
            "modified",
        )
        read_only_fields = (
            "id",
            "slug",
            "created",
            "modified",
        )
