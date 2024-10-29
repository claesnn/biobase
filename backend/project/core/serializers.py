"""Serializers for the core app."""

from jsonschema import ValidationError as JsonSchemaValidationError
from jsonschema import validate
from rest_framework import serializers

from .models import MetadataSchema, Sample


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

        schema = attrs.get("schema")
        metadata = attrs.get("metadata")

        try:
            validate(instance=metadata, schema=schema.definition)
        except JsonSchemaValidationError as e:
            raise serializers.ValidationError(f"Metadata validation error: {e.message}")

        return attrs
