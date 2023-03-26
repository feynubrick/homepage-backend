from django.views.generic import ListView, DetailView

from project.apps.wiki.models import Article


class ArticleListView(ListView):
    model = Article


class ArticleDetailView(DetailView):
    model = Article

