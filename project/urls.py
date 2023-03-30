from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("wiki/", include("project.apps.wiki.urls", namespace="wiki")),
]
