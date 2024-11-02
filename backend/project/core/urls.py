"""URLs for the core app."""

from rest_framework.routers import DefaultRouter

from .views import (
    EntitySchemaViewset,
    EntityViewSet,
    ResultSchemaViewSet,
    ResultViewSet,
    SampleSchemaViewSet,
    SampleViewSet,
)

router = DefaultRouter()
router.register(r"sample-schemas", SampleSchemaViewSet, basename="sample-schema")
router.register(r"samples", SampleViewSet, basename="sample")
router.register(r"result-schemas", ResultSchemaViewSet, basename="result-schema")
router.register(r"results", ResultViewSet, basename="result")
router.register(r"entities", EntityViewSet, basename="entity")
router.register(r"entity-schemas", EntitySchemaViewset, basename="entity-schema")

urlpatterns = router.urls
