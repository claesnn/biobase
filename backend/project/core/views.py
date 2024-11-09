"""Views for the core app."""

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Analysis, Batch, Entity, MetaSchema, Project, Result, Sample
from .serializers import (
    AnalysisSerializer,
    BatchSerializer,
    EntitySerializer,
    MetaSchemaSerializer,
    ProjectSerializer,
    ResultSerializer,
    SampleSerializer,
)


class ProjectViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing projects.
    """

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class MetaSchemaViewset(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing metadata schemas.
    """

    queryset = MetaSchema.objects.all()
    serializer_class = MetaSchemaSerializer


class EntityViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing entities.
    """

    queryset = Entity.objects.select_related("schema")
    serializer_class = EntitySerializer

    def get_queryset(self):
        """
        Optionally restricts the returned entities to a given schema type or version,
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


class BatchViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing batches.
    """

    queryset = Batch.objects.select_related("schema")
    serializer_class = BatchSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned batches to a given schema type or version,
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

    @action(detail=True, methods=["get"])
    def results(self, request, pk=None):
        """
        Return all results associated with a sample.
        """
        sample = self.get_object()
        results = sample.results.all()
        serializer = ResultSerializer(results, many=True)
        return Response(serializer.data)


class AnalysisViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing analyses.
    """

    queryset = Analysis.objects.select_related("schema")
    serializer_class = AnalysisSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned analyses to a given schema type or version,
        by filtering against `schema__type` and `schema__version` query parameters in the URL.
        """
        queryset = self.queryset
        schema_type = self.request.query_params.get("schema__type")
        schema_version = self.request.query_params.get("schema__version")

        if schema_type:
            queryset = queryset.filter(schema__type=schema_type)
        if schema_version:
            queryset = queryset.filter(schema__version=schema_version)

        return queryset


class ResultViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing results associated with samples.
    """

    queryset = Result.objects.select_related("schema")
    serializer_class = ResultSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned results to a given schema type or version,
        by filtering against `schema__type` and `schema__version` query parameters in the URL.
        """
        queryset = self.queryset
        schema_type = self.request.query_params.get("schema__type")
        schema_version = self.request.query_params.get("schema__version")

        if schema_type:
            queryset = queryset.filter(schema__type=schema_type)
        if schema_version:
            queryset = queryset.filter(schema__version=schema_version)

        return queryset
