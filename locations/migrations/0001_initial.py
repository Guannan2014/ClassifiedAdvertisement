# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Country'
        db.create_table(u'locations_country', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name_eng', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('name_gbk', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('name_bg5', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'locations', ['Country'])

        # Adding model 'State'
        db.create_table(u'locations_state', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name_eng', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('name_gbk', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('name_bg5', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['locations.Country'])),
        ))
        db.send_create_signal(u'locations', ['State'])

        # Adding model 'City'
        db.create_table(u'locations_city', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name_eng', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('name_gbk', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('name_bg5', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('state', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['locations.State'])),
        ))
        db.send_create_signal(u'locations', ['City'])

        # Adding model 'District'
        db.create_table(u'locations_district', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name_eng', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('name_gbk', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('name_bg5', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['locations.City'])),
        ))
        db.send_create_signal(u'locations', ['District'])


    def backwards(self, orm):
        # Deleting model 'Country'
        db.delete_table(u'locations_country')

        # Deleting model 'State'
        db.delete_table(u'locations_state')

        # Deleting model 'City'
        db.delete_table(u'locations_city')

        # Deleting model 'District'
        db.delete_table(u'locations_district')


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
        u'locations.country': {
            'Meta': {'object_name': 'Country'},
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