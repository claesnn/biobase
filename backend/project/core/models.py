"""Core models for samples and metadata schema"""

from django.db import models
from django.db.models import JSONField


class MetadataSchema(models.Model):
    """Metadata schema for samples"""

    type = models.CharField(max_length=100)
    version = models.PositiveSmallIntegerField()
    definition = JSONField()

    class Meta:
        """Ensure unique schema type and version"""

        unique_together = ("type", "version")

    def __str__(self):
        return f"{self.type} v{self.version}"


class Sample(models.Model):
    """Sample with metadata"""

    sample_id = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    requestor_id = models.CharField(max_length=100)
    schema = models.ForeignKey(MetadataSchema, on_delete=models.PROTECT)
    metadata = JSONField()

    def __str__(self):
        return f"{self.sample_id} ({self.schema})"


class ResultSchema(models.Model):
    """Schema for validating Result metadata"""

    type = models.CharField(max_length=100)
    version = models.PositiveSmallIntegerField()
    definition = JSONField()

    class Meta:
        unique_together = ("type", "version")

    def __str__(self):
        return f"{self.type} v{self.version}"


class Result(models.Model):
    """Result associated with a sample, validated by ResultSchema"""

    sample = models.ForeignKey(Sample, on_delete=models.CASCADE, related_name="results")
    schema = models.ForeignKey(ResultSchema, on_delete=models.PROTECT)
    data = JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Result for {self.sample} ({self.schema})"
