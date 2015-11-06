from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^(?P<city_code>\w{3})/(?P<category_code>\w{1})/$', 
       'categories.views.category_view', 
       name='category_view'),
)