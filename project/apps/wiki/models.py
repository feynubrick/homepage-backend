from django.db import models
from project.commons.models import BaseTimestampedModel


class Article(BaseTimestampedModel):
    deleted = models.BooleanField(help_text="flag for delete", default=False)
    parent = models.ForeignKey("self", related_name="children", on_delete=models.CASCADE, null=True, blank=True)
    slug = models.TextField(max_length=200, help_text="Article ID for URL")
    head_revision = models.ForeignKey(
        "ArticleRevision", on_delete=models.SET_NULL, related_name="article_as_head", null=True, blank=True
    )


class ArticleRevision(BaseTimestampedModel):
    article = models.ForeignKey("Article", on_delete=models.CASCADE, related_name="revisions")
    title = models.TextField(max_length=100, help_text="Title", db_index=True)
    body = models.TextField(help_text="Article body")
    deleted = models.BooleanField(help_text="Flag for delete", db_index=True)
