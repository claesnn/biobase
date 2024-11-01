# Generated by Django 5.1.2 on 2024-10-30 20:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MetadataSchema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('version', models.PositiveSmallIntegerField()),
                ('definition', models.JSONField()),
            ],
            options={
                'unique_together': {('type', 'version')},
            },
        ),
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('metadata', models.JSONField()),
                ('schema', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.metadataschema')),
            ],
        ),
        migrations.CreateModel(
            name='ResultSchema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('version', models.PositiveSmallIntegerField()),
                ('definition', models.JSONField()),
            ],
            options={
                'unique_together': {('type', 'version')},
            },
        ),
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('requestor_id', models.CharField(max_length=100)),
                ('metadata', models.JSONField()),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='samples', to='core.entity')),
                ('schema', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.metadataschema')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.JSONField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('schema', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.resultschema')),
                ('sample', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', to='core.sample')),
            ],
        ),
    ]
