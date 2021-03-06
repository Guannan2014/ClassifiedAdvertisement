from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^(?P<city_code>\w{3})/$', 
		'locations.views.city_view', 
		name='city_view'),
    url(r'^$', 
    	'locations.views.index', 
    	name='index'),
    url(r'^cities/$', 
    	'locations.views.reset_city', 
    	name='reset_city'),
)