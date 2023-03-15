from django.db import models


class BaseModel(models.Model):
    class Meta:
        abstract = True


class BaseTimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, help_text="Timestamp on create", db_index=True)
    updated_at = models.DateTimeField(auto_now=True, help_text="Timestamp on update", db_index=True)

    class Meta:
        abstract = True
