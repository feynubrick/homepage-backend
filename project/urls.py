from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from project.apis.wiki.article_views import ArticleViewSet


router = routers.DefaultRouter()
router.register(r"articles", ArticleViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path("admin/", admin.site.urls),
    path("wiki/", include("project.apps.wiki.urls", namespace="wiki")),
]
