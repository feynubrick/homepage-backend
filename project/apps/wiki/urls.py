from django.urls import path
from .views import ArticleListView, ArticleDetailView, ArticleCreateView


app_name = "wiki"
urlpatterns = [
    path(route="", view=ArticleListView.as_view(), name="home"),
    path(route="articles/", view=ArticleListView.as_view(), name="article_list"),
    path(route="articles/add/", view=ArticleCreateView.as_view(), name="article_add"),
    path(route="articles/<slug:slug>/", view=ArticleDetailView.as_view(), name="article_detail"),
]
