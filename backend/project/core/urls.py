"""URLs for the core app."""

from rest_framework.routers import DefaultRouter

from .views import (
    MetadataSchemaViewSet,
    ResultSchemaViewSet,
    ResultViewSet,
    SampleViewSet,
)

router = DefaultRouter()
router.register(r"metadata-schemas", MetadataSchemaViewSet, basename="metadata-schema")
router.register(r"samples", SampleViewSet, basename="sample")
router.register(r"result-schemas", ResultSchemaViewSet, basename="result-schema")
router.register(r"results", ResultViewSet, basename="result")

urlpatterns = router.urls
