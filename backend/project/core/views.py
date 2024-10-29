"""Views for the core app."""

from rest_framework import viewsets

from .models import MetadataSchema, Sample
from .serializers import MetadataSchemaSerializer, SampleSerializer


class MetadataSchemaViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing metadata schemas.
    """

    queryset = MetadataSchema.objects.all()
    serializer_class = MetadataSchemaSerializer


class SampleViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing samples.
    """

    queryset = Sample.objects.select_related("schema")
    serializer_class = SampleSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned samples to a given schema type or version,
        by filtering against `schema__type` and `schema__version` query parameters in the URL.
        """
        queryset = super().get_queryset()
        schema_type = self.request.query_params.get("schema__type")
        schema_version = self.request.query_params.get("schema__version")

        if schema_type:
            queryset = queryset.filter(schema__type=schema_type)
        if schema_version:
            queryset = queryset.filter(schema__version=schema_version)

        return queryset
