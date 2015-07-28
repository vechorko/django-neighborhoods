# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Neighborhood',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('state', models.CharField(max_length=2, db_index=True)),
                ('city', models.CharField(max_length=90)),
                ('name', models.CharField(max_length=90)),
                ('geog', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326, geography=True)),
                ('region_id', models.FloatField(null=True, blank=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='NeighborhoodSource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('priority', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='neighborhood',
            name='source',
            field=models.ForeignKey(blank=True, to='neighborhoods.NeighborhoodSource', null=True),
        ),
        migrations.AlterUniqueTogether(
            name='neighborhood',
            unique_together=set([('source', 'state', 'city', 'name', 'region_id')]),
        ),
    ]
