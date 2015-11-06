# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Neighborhood'
        db.delete_table(u'locations_neighborhood')

        # Adding model 'Hood'
        db.create_table(u'locations_hood', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name_eng', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('name_gbk', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('name_bg5', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=30, blank=True)),
            ('district', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['locations.District'])),
        ))
        db.send_create_signal(u'locations', ['Hood'])


    def backwards(self, orm):
        # Adding model 'Neighborhood'
        db.create_table(u'locations_neighborhood', (
            ('district', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['locations.District'])),
            ('name_gbk', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=30)),
            ('name_bg5', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('name_eng', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'locations', ['Neighborhood'])

        # Deleting model 'Hood'
        db.delete_table(u'locations_hood')


    models = {
        u'locations.city': {
            'Meta': {'object_name': 'City'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_bg5': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'name_eng': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'name_gbk': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '30', 'blank': 'True'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['locations.State']"})
        },
        u'locations.continent': {
            'Meta': {'object_name': 'Continent'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_bg5': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'name_eng': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'name_gbk': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '30', 'blank': 'True'})
        },
        u'locations.country': {
            'Meta': {'object_name': 'Country'},
            'continent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['locations.Continent']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_bg5': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'name_eng': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'name_gbk': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '30', 'blank': 'True'})
        },
        u'locations.district': {
            'Meta': {'object_name': 'District'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['locations.City']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_bg5': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'name_eng': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'name_gbk': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '30', 'blank': 'True'})
        },
        u'locations.hood': {
            'Meta': {'object_name': 'Hood'},
            'district': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['locations.District']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_bg5': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'name_eng': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'name_gbk': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '30', 'blank': 'True'})
        },
        u'locations.state': {
            'Meta': {'object_name': 'State'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['locations.Country']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_bg5': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'name_eng': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'name_gbk': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '30', 'blank': 'True'})
        }
    }

    complete_apps = ['locations']