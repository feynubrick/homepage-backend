from django.db import models
from django.utils.translation import gettext_lazy as _


class ArticleType(models.TextChoices):
    BIBLIOGRAPHY = "BIB", _("Bibliography")
