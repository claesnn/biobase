"""Core models for samples and metadata schema"""

from django.db import models
from django.db.models import JSONField


class Project(models.Model):
    """Project model"""

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class MetaSchema(models.Model):
    """Schema for validating Entity metadata"""

    class SchemaType(models.IntegerChoices):
        """Schema type (Entity, Batch, Sample, Result)"""

        ENTITY = 1
        BATCH = 2
        SAMPLE = 3
        RESULT = 4
        ANALYSIS = 5
        MATERIAL = 6

    title = models.CharField(
        max_length=100
    )  # Antibody, Cultivation, CultivationSample, Plasmid, Stem Cell, Oligo
    type = models.IntegerField(choices=SchemaType)
    version = models.PositiveSmallIntegerField()
    definition = JSONField()

    class Meta:
        unique_together = ("title", "type", "version")

    def __str__(self):
        return f"{self.type} v{self.version}"


class Entity(models.Model):
    """Entity with metadata"""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    schema = models.ForeignKey(MetaSchema, on_delete=models.PROTECT)
    projects = models.ManyToManyField(Project, related_name="entities")
    metadata = JSONField()

    @property
    def barcode(self):
        """Return barcode for the entity"""
        prefix = self.metadata.get("prefix", "XX")
        return f"{prefix}{self.id}"

    def __str__(self):
        prefix = self.metadata.get("prefix", "XX")
        return f"{prefix}{self.id}"


class Material(models.Model):
    """Material model"""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    metadata = JSONField()

    entity = models.ForeignKey(
        Entity, on_delete=models.PROTECT, related_name="materials"
    )
    schema = models.ForeignKey(MetaSchema, on_delete=models.PROTECT)
    projects = models.ManyToManyField(Project, related_name="materials")

    @property
    def barcode(self):
        """Return barcode for the material"""
        prefix = "M"
        return f"{prefix}{self.id}"

    def __str__(self):
        return f"Material {self.id}"


class Batch(models.Model):
    """Batch of preparations"""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    metadata = JSONField()

    schema = models.ForeignKey(MetaSchema, on_delete=models.PROTECT)
    projects = models.ManyToManyField(Project, related_name="batches")
    preparations = models.ManyToManyField(Entity, related_name="batches")

    @property
    def barcode(self):
        """Return barcode for the batch"""
        prefix = "B"
        return f"{prefix}{self.id}"

    def __str__(self):
        return f"Batch {self.id}"


class Sample(models.Model):
    """Sample with metadata"""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    metadata = JSONField()

    batch = models.ForeignKey(Batch, on_delete=models.PROTECT, related_name="samples")
    schema = models.ForeignKey(MetaSchema, on_delete=models.PROTECT)

    @property
    def barcode(self):
        """Return barcode for the sample"""
        prefix = "S"
        return f"{prefix}{self.id}"

    def __str__(self):
        return f"{self.id} ({self.schema})"


class Analysis(models.Model):
    """Analysis model representing an analytical run (e.g., HPLC SEC for titer quantification)"""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    schema = models.ForeignKey(MetaSchema, on_delete=models.PROTECT)
    metadata = JSONField()
    projects = models.ManyToManyField(Project, related_name="analyses")
    raw_data_link = models.URLField(blank=True, null=True, help_text="Link to raw data")

    @property
    def barcode(self):
        """Return barcode for the analysis"""
        prefix = "A"
        return f"{prefix}{self.id}"

    def __str__(self):
        return f"Analysis {self.id}"


class Result(models.Model):
    """Result model linking to both Analysis and Sample, storing specific output data"""

    analysis = models.ForeignKey(
        Analysis, on_delete=models.CASCADE, related_name="results"
    )
    sample = models.ForeignKey(Sample, on_delete=models.CASCADE, related_name="results")
    schema = models.ForeignKey(MetaSchema, on_delete=models.PROTECT)
    data = JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def barcode(self):
        """Return barcode for the result"""
        prefix = "R"
        return f"{prefix}{self.id}"

    def __str__(self):
        return f"Result for Sample {self.sample.id}"
