# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'District'
        db.delete_table(u'locations_district')

        # Adding model 'Subarea'
        db.create_table(u'locations_subarea', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name_eng', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('name_gbk', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('name_bg5', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=30, blank=True)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['locations.City'])),
        ))
        db.send_create_signal(u'locations', ['Subarea'])

        # Deleting field 'Hood.district'
        db.delete_column(u'locations_hood', 'district_id')

        # Adding field 'Hood.subarea'
        db.add_column(u'locations_hood', 'subarea',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['locations.Subarea']),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'District'
        db.create_table(u'locations_district', (
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['locations.City'])),
            ('name_gbk', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=30, blank=True)),
            ('name_bg5', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('name_eng', self.gf('django.db.models.fields.CharField')(max_length=30)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'locations', ['District'])

        # Deleting model 'Subarea'
        db.delete_table(u'locations_subarea')

        # Adding field 'Hood.district'
        db.add_column(u'locations_hood', 'district',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['locations.District']),
                      keep_default=False)

        # Deleting field 'Hood.subarea'
        db.delete_column(u'locations_hood', 'subarea_id')


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
        u'locations.hood': {
            'Meta': {'object_name': 'Hood'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_bg5': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'name_eng': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'name_gbk': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '30', 'blank': 'True'}),
            'subarea': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['locations.Subarea']"})
        },
        u'locations.state': {
            'Meta': {'object_name': 'State'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['locations.Country']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_bg5': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'name_eng': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'name_gbk': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '30', 'blank': 'True'})
        },
        u'locations.subarea': {
            'Meta': {'object_name': 'Subarea'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['locations.City']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_bg5': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'name_eng': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'name_gbk': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '30', 'blank': 'True'})
        }
    }

    complete_apps = ['locations']