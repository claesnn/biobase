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
    metadata = JSONField(blank=True, null=True)

    def __str__(self):
        return f"{self.sample_id} ({self.schema})"
