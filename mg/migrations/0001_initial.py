# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import mg.models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('object_id', models.PositiveIntegerField()),
                ('photo', models.ImageField(upload_to='mg/%Y/')),
                ('dateCreated', models.DateTimeField()),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
            ],
            options={
                'ordering': ['dateCreated'],
            },
        ),
        migrations.CreateModel(
            name='Planting',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('amount', models.IntegerField()),
                ('plantedTime', models.DateTimeField()),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
            ],
            bases=(models.Model, mg.models.MGMixin),
        ),
        migrations.CreateModel(
            name='PlantingLocation',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('location', models.CharField(max_length=100)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Planting Location',
            },
            bases=(models.Model, mg.models.MGMixin),
        ),
        migrations.CreateModel(
            name='SeedBatch',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('label', models.CharField(max_length=10, blank=True)),
                ('source', models.CharField(choices=[('Collected', 'Collected'), ('Living Seeds', 'Living Seeds'), ('Stark Ayres', 'Stark Ayres'), ('Mayford', 'Mayford'), ('Kirchoffs', 'Kirchoffs'), ('GardenMaster', 'GardenMaster')], max_length=20)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
            ],
            bases=(models.Model, mg.models.MGMixin),
        ),
        migrations.CreateModel(
            name='Transplant',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('amount', models.IntegerField()),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('fromLocation', models.ForeignKey(to='mg.PlantingLocation', related_name='transplantsOut')),
                ('seedBatch', models.ForeignKey(to='mg.SeedBatch')),
                ('toLocation', models.ForeignKey(to='mg.PlantingLocation', related_name='transplantsIn')),
            ],
            bases=(models.Model, mg.models.MGMixin),
        ),
        migrations.CreateModel(
            name='Variety',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('species', models.CharField(max_length=40)),
                ('variety', models.CharField(max_length=100, blank=True)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
            ],
            bases=(models.Model, mg.models.MGMixin),
        ),
        migrations.AddField(
            model_name='seedbatch',
            name='variety',
            field=models.ForeignKey(to='mg.Variety'),
        ),
        migrations.AddField(
            model_name='planting',
            name='location',
            field=models.ForeignKey(to='mg.PlantingLocation'),
        ),
        migrations.AddField(
            model_name='planting',
            name='seedBatch',
            field=models.ForeignKey(to='mg.SeedBatch'),
        ),
    ]
