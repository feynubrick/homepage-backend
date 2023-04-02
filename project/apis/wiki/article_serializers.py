from rest_framework import serializers
from project.apps.wiki.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ["id", "title", "body", "slug", "deleted"]
