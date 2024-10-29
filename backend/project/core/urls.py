"""URLs for the core app."""

from rest_framework.routers import DefaultRouter

from .views import MetadataSchemaViewSet, SampleViewSet

router = DefaultRouter()
router.register(r"metadata-schemas", MetadataSchemaViewSet, basename="metadata-schema")
router.register(r"samples", SampleViewSet, basename="sample")

urlpatterns = router.urls
