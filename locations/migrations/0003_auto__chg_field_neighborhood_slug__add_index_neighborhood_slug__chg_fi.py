# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Neighborhood.slug'
        db.alter_column(u'locations_neighborhood', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=30))
        # Adding index on 'Neighborhood', fields ['slug']
        db.create_index(u'locations_neighborhood', ['slug'])


        # Changing field 'City.slug'
        db.alter_column(u'locations_city', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=30))
        # Adding index on 'City', fields ['slug']
        db.create_index(u'locations_city', ['slug'])


        # Changing field 'District.slug'
        db.alter_column(u'locations_district', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=30))
        # Adding index on 'District', fields ['slug']
        db.create_index(u'locations_district', ['slug'])


        # Changing field 'Continent.slug'
        db.alter_column(u'locations_continent', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=30))
        # Adding index on 'Continent', fields ['slug']
        db.create_index(u'locations_continent', ['slug'])


        # Changing field 'State.slug'
        db.alter_column(u'locations_state', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=30))
        # Adding index on 'State', fields ['slug']
        db.create_index(u'locations_state', ['slug'])


        # Changing field 'Country.slug'
        db.alter_column(u'locations_country', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=30))
        # Adding index on 'Country', fields ['slug']
        db.create_index(u'locations_country', ['slug'])


    def backwards(self, orm):
        # Removing index on 'Country', fields ['slug']
        db.delete_index(u'locations_country', ['slug'])

        # Removing index on 'State', fields ['slug']
        db.delete_index(u'locations_state', ['slug'])

        # Removing index on 'Continent', fields ['slug']
        db.delete_index(u'locations_continent', ['slug'])

        # Removing index on 'District', fields ['slug']
        db.delete_index(u'locations_district', ['slug'])

        # Removing index on 'City', fields ['slug']
        db.delete_index(u'locations_city', ['slug'])

        # Removing index on 'Neighborhood', fields ['slug']
        db.delete_index(u'locations_neighborhood', ['slug'])


        # Changing field 'Neighborhood.slug'
        db.alter_column(u'locations_neighborhood', 'slug', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'City.slug'
        db.alter_column(u'locations_city', 'slug', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'District.slug'
        db.alter_column(u'locations_district', 'slug', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'Continent.slug'
        db.alter_column(u'locations_continent', 'slug', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'State.slug'
        db.alter_column(u'locations_state', 'slug', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'Country.slug'
        db.alter_column(u'locations_country', 'slug', self.gf('django.db.models.fields.CharField')(max_length=30))

    models = {
        u'locations.city': {
            'Meta': {'object_name': 'City'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_bg5': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'name_eng': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'name_gbk': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '30'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['locations.State']"})
        },
        u'locations.continent': {
            'Meta': {'object_name': 'Continent'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_bg5': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'name_eng': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'name_gbk': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '30'})
        },
        u'locations.country': {
            'Meta': {'object_name': 'Country'},
            'continent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['locations.Continent']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_bg5': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'name_eng': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'name_gbk': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '30'})
        },
        u'locations.district': {
            'Meta': {'object_name': 'District'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['locations.City']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_bg5': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'name_eng': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'name_gbk': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '30'})
        },
        u'locations.neighborhood': {
            'Meta': {'object_name': 'Neighborhood'},
            'district': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['locations.District']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_bg5': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'name_eng': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'name_gbk': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '30'})
        },
        u'locations.state': {
            'Meta': {'object_name': 'State'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['locations.Country']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_bg5': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'name_eng': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'name_gbk': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['locations']