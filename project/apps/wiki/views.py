from django.views.generic import ListView, DetailView, CreateView

from project.apps.wiki.models import Article


class ArticleListView(ListView):
    model = Article


class ArticleDetailView(DetailView):
    model = Article


class ArticleCreateView(CreateView):
    model = Article
    fields = [
        "title",
        "slug",
        "body",
    ]
