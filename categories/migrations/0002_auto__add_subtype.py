# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Subtype'
        db.create_table(u'categories_subtype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name_eng', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('name_gbk', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('name_bg5', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=30)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['categories.Subcategory'])),
        ))
        db.send_create_signal(u'categories', ['Subtype'])


    def backwards(self, orm):
        # Deleting model 'Subtype'
        db.delete_table(u'categories_subtype')


    models = {
        u'categories.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_bg5': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'name_eng': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'name_gbk': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '30'})
        },
        u'categories.subcategory': {
            'Meta': {'object_name': 'Subcategory'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['categories.Category']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_bg5': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'name_eng': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'name_gbk': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '30'})
        },
        u'categories.subtype': {
            'Meta': {'object_name': 'Subtype'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['categories.Subcategory']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_bg5': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'name_eng': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'name_gbk': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['categories']