"""Serializers for the core app."""

from jsonschema import ValidationError as JsonSchemaValidationError
from jsonschema import validate
from rest_framework import serializers

from .models import Entity, MetadataSchema, Result, ResultSchema, Sample


class MetadataSchemaSerializer(serializers.ModelSerializer):
    """Serializer for the MetadataSchema model."""

    class Meta:
        model = MetadataSchema
        fields = "__all__"


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


class ResultSchemaSerializer(serializers.ModelSerializer):
    """Serializer for the ResultSchema model."""

    class Meta:
        model = ResultSchema
        fields = "__all__"


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
