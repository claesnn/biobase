"""Serializers for the core app."""

from jsonschema import ValidationError as JsonSchemaValidationError
from jsonschema import validate
from rest_framework import serializers

from .models import Analysis, Batch, Entity, MetaSchema, Project, Result, Sample


class ProjectSerializer(serializers.ModelSerializer):
    """Serializer for the Project model."""

    class Meta:
        model = Project
        fields = "__all__"


class MetaSchemaSerializer(serializers.ModelSerializer):
    """Serializer for the MetadataSchema model."""

    class Meta:
        model = MetaSchema
        fields = "__all__"


class EntitySerializer(serializers.ModelSerializer):
    """Serializer for the Entity model."""

    class Meta:
        model = Entity
        fields = "__all__"

    def validate(self, attrs):
        attrs = super().validate(attrs)

        try:
            validate(instance=attrs["metadata"], schema=attrs["schema"].definition)
        except JsonSchemaValidationError as e:
            raise serializers.ValidationError(f"Metadata validation error: {e.message}")

        return attrs


class BatchSerializer(serializers.ModelSerializer):
    """Serializer for the Batch model."""

    class Meta:
        model = Batch
        fields = "__all__"

    def validate(self, attrs):
        attrs = super().validate(attrs)

        try:
            validate(instance=attrs["metadata"], schema=attrs["schema"].definition)
        except JsonSchemaValidationError as e:
            raise serializers.ValidationError(f"Metadata validation error: {e.message}")

        return attrs


class SampleSerializer(serializers.ModelSerializer):
    """Serializer for the Sample model."""

    class Meta:
        model = Sample
        fields = "__all__"

    def validate(self, attrs):
        attrs = super().validate(attrs)

        try:
            validate(instance=attrs["metadata"], schema=attrs["schema"].definition)
        except JsonSchemaValidationError as e:
            raise serializers.ValidationError(f"Metadata validation error: {e.message}")

        return attrs


class AnalysisSerializer(serializers.ModelSerializer):
    """Serializer for the Analysis model."""

    class Meta:
        model = Analysis
        fields = "__all__"

    def validate(self, attrs):
        attrs = super().validate(attrs)

        try:
            validate(instance=attrs["metadata"], schema=attrs["schema"].definition)
        except JsonSchemaValidationError as e:
            raise serializers.ValidationError(f"Metadata validation error: {e.message}")

        return attrs


class ResultSerializer(serializers.ModelSerializer):
    """Serializer for the Result model."""

    class Meta:
        model = Result
        fields = "__all__"

    def validate(self, attrs):
        attrs = super().validate(attrs)

        try:
            validate(instance=attrs["data"], schema=attrs["schema"].definition)
        except JsonSchemaValidationError as e:
            raise serializers.ValidationError(
                f"Result data validation error: {e.message}"
            )

        return attrs
