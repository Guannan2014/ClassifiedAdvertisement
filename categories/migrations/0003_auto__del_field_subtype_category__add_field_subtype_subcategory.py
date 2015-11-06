# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Subtype.category'
        db.delete_column(u'categories_subtype', 'category_id')

        # Adding field 'Subtype.subcategory'
        db.add_column(u'categories_subtype', 'subcategory',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['categories.Subcategory']),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Subtype.category'
        db.add_column(u'categories_subtype', 'category',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['categories.Subcategory']),
                      keep_default=False)

        # Deleting field 'Subtype.subcategory'
        db.delete_column(u'categories_subtype', 'subcategory_id')


    models = {
        u'categories.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_bg5': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'name_eng': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'name_gbk': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '30', 'blank': 'True'})
        },
        u'categories.subcategory': {
            'Meta': {'object_name': 'Subcategory'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['categories.Category']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_bg5': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'name_eng': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'name_gbk': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '30', 'blank': 'True'})
        },
        u'categories.subtype': {
            'Meta': {'object_name': 'Subtype'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_bg5': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'name_eng': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'name_gbk': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '30', 'blank': 'True'}),
            'subcategory': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['categories.Subcategory']"})
        }
    }

    complete_apps = ['categories']