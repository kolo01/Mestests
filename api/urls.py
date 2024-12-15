from django.urls import path, include
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import routers

from stocks.viewsets.article_viewsets import ArticleViewSet
from stocks.viewsets.intrant_viewsets import IntrantViewSet
from stocks.viewsets.providers_viewsets import ProviderViewSet
from stocks.viewsets.product_type_viewsets import ProductTypeViewSet





schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


router = routers.DefaultRouter()
router.register(r'article', ArticleViewSet)
router.register(r'intrant', IntrantViewSet)
router.register(r'product type', ProductTypeViewSet)
router.register(r'provider', ProviderViewSet)


urlpatterns = [
path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
path('', include(router.urls)),
]
