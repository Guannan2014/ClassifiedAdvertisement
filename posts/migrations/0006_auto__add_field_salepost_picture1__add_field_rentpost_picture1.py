# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'SalePost.picture1'
        db.add_column(u'posts_salepost', 'picture1',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=256, null=True, blank=True),
                      keep_default=False)

        # Adding field 'RentPost.picture1'
        db.add_column(u'posts_rentpost', 'picture1',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=256, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'SalePost.picture1'
        db.delete_column(u'posts_salepost', 'picture1')

        # Deleting field 'RentPost.picture1'
        db.delete_column(u'posts_rentpost', 'picture1')


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
        },
        u'posts.rentpost': {
            'Meta': {'object_name': 'RentPost'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'approved': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['locations.City']"}),
            'contact_person': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'details': ('django.db.models.fields.TextField', [], {'max_length': '3000', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'picture1': ('django.db.models.fields.files.ImageField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'qq': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'rent_out': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'structure': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'}),
            'subarea': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['locations.Subarea']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'total_baths': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'total_rooms': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'weixin': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'})
        },
        u'posts.salepost': {
            'Meta': {'object_name': 'SalePost'},
            'approved': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['locations.City']"}),
            'contact_person': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'details': ('django.db.models.fields.TextField', [], {'max_length': '3000', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'picture1': ('django.db.models.fields.files.ImageField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'qq': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'subarea': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['locations.Subarea']", 'null': 'True', 'blank': 'True'}),
            'subcat': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['categories.Subcategory']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'weight': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'weixin': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'})
        }
    }

    complete_apps = ['posts']