from django.db import models

from project.commons.models import BaseTimestampedModel


class Article(BaseTimestampedModel):
    deleted = models.BooleanField(help_text="flag for delete", default=False)
    title = models.TextField(max_length=100, help_text="Title", db_index=True)
    body = models.TextField(help_text="Article body")
    slug = models.TextField(max_length=200, help_text="Article ID for URL", db_index=True, unique=True)
