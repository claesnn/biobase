"""URLs for the core app."""

from rest_framework.routers import DefaultRouter

from .views import (
    AnalysisViewSet,
    BatchViewSet,
    EntityViewSet,
    MetaSchemaViewset,
    ProjectViewSet,
    ResultViewSet,
    SampleViewSet,
)

router = DefaultRouter()
router.register(r"projects", ProjectViewSet, basename="project")
router.register(r"metaschemas", MetaSchemaViewset, basename="metaschema")
router.register(r"entities", EntityViewSet, basename="entity")
router.register(r"batches", BatchViewSet, basename="batch")
router.register(r"samples", SampleViewSet, basename="sample")
router.register(r"analyses", AnalysisViewSet, basename="analysis")
router.register(r"results", ResultViewSet, basename="result")

urlpatterns = router.urls
