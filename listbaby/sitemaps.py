from datetime import datetime
from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse
from posts.models import *

class CitySitemap(Sitemap):
	changefreq = "weekly"
	priority = 0.6
	# remember to modify when adding new cities	
	def items(self):
		return City.objects.exclude(id__in=(4, 5))

	def location(self, item):
		return '/' + item.slug + '/'

class RentPostSitemap(Sitemap):
	changefreq = "weekly"
	priority = 0.4

	def items(self):
		return RentPost.objects.all().prefetch_related('city', 'cat')

	def lastmod(self, obj):
		return obj.modified

	def location(self, obj):
		city = obj.city.slug
		cat = obj.cat.slug
		obj_id = str(obj.id)
		url_string = '/' + city + '/' + cat + '/' + obj_id
		return url_string

class SalePostSitemap(Sitemap):
	changefreq = "weekly"
	priority = 0.4

	def items(self):
		return SalePost.objects.all().prefetch_related('city', 'cat')

	def lastmod(self, obj):
		return obj.modified

	def location(self, obj):
		city = obj.city.slug
		cat = obj.cat.slug
		obj_id = str(obj.id)
		url_string = '/' + city + '/' + cat + '/' + obj_id
		return url_string

class StaticViewSitemap(Sitemap):
	changefreq = "monthly"
	priority = 0.4

	def items(self):
		return ['about', 
				'terms', 
				'privacy', 
				'safety', 
				'contact', 
				'upgrade']

	def location(self, item):
		return reverse(item)
