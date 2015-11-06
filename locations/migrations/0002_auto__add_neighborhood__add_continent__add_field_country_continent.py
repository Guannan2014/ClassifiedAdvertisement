# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Neighborhood'
        db.create_table(u'locations_neighborhood', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name_eng', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('name_gbk', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('name_bg5', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('district', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['locations.District'])),
        ))
        db.send_create_signal(u'locations', ['Neighborhood'])

        # Adding model 'Continent'
        db.create_table(u'locations_continent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name_eng', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('name_gbk', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('name_bg5', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'locations', ['Continent'])

        # Adding field 'Country.continent'
        db.add_column(u'locations_country', 'continent',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['locations.Continent'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Neighborhood'
        db.delete_table(u'locations_neighborhood')

        # Deleting model 'Continent'
        db.delete_table(u'locations_continent')

        # Deleting field 'Country.continent'
        db.delete_column(u'locations_country', 'continent_id')


    models = {
        u'locations.city': {
            'Meta': {'object_name': 'City'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_bg5': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'name_eng': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'name_gbk': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['locations.State']"})
        },
        u'locations.continent': {
            'Meta': {'object_name': 'Continent'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_bg5': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'name_eng': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'name_gbk': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'locations.country': {
            'Meta': {'object_name': 'Country'},
            'continent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['locations.Continent']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_bg5': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'name_eng': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'name_gbk': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'locations.district': {
            'Meta': {'object_name': 'District'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['locations.City']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_bg5': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'name_eng': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'name_gbk': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'locations.neighborhood': {
            'Meta': {'object_name': 'Neighborhood'},
            'district': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['locations.District']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_bg5': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'name_eng': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'name_gbk': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'locations.state': {
            'Meta': {'object_name': 'State'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['locations.Country']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_bg5': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'name_eng': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'name_gbk': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['locations']