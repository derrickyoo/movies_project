import uuid

from django.db import models

from autoslug import AutoSlugField
from model_utils.models import TimeStampedModel


class Movie(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("Title", max_length=255)
    slug = AutoSlugField(
        "Movie Address",
        unique=True,
        always_update=False,
        populate_from="title",
    )
    genre = models.CharField("Genre", max_length=255)
    year = models.CharField("Year", max_length=4)

    def __str__(self):
        return f"{self.title}"
