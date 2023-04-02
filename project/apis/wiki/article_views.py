from rest_framework import viewsets

from project.apps.wiki.models import Article

from .article_serializers import ArticleSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
