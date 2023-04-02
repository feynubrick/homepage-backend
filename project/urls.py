from django.urls import path, include, re_path

from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from project.apis.wiki.article_views import ArticleViewSet


router = routers.DefaultRouter()
router.register(r"articles", ArticleViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="Homepage API",
      default_version="v1",
      description="API for homepage project",
      contact=openapi.Contact(email="feynubrick@proton.me"),
      license=openapi.License(name="MIT"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    re_path(r"^swagger(?P<format>\.json|\.yaml)$", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    re_path(r"^swagger/$", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("", include(router.urls)),
]
