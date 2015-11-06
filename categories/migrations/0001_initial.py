# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_eng', models.CharField(max_length=30)),
                ('name_gbk', models.CharField(max_length=30, blank=True)),
                ('name_bg5', models.CharField(max_length=30, blank=True)),
                ('slug', models.SlugField(max_length=30, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_eng', models.CharField(max_length=30)),
                ('name_gbk', models.CharField(max_length=30, blank=True)),
                ('name_bg5', models.CharField(max_length=30, blank=True)),
                ('slug', models.SlugField(max_length=30, blank=True)),
                ('category', models.ForeignKey(to='categories.Category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Subtype',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_eng', models.CharField(max_length=30)),
                ('name_gbk', models.CharField(max_length=30, blank=True)),
                ('name_bg5', models.CharField(max_length=30, blank=True)),
                ('slug', models.SlugField(max_length=30, blank=True)),
                ('subcategory', models.ForeignKey(to='categories.Subcategory')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
