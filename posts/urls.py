from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^(?P<city_code>\w{3})/post/$', 
       'posts.views.post_type', 
       name='post_type'),
    url(r'^(?P<city_code>\w{3})/post/thanks/$', 
        'posts.views.post_thanks', 
        name='post_thanks'),
    url(r'^(?P<city_code>\w{3})/(?P<category_code>\w{1})/(?P<post_id>\d+)/$', 
       'posts.views.single_post', 
       name='single_post'),
    url(r'^(?P<city_code>\w{3})/post/(?P<post_type>\w{3})/$', 
       'posts.views.new_post', 
       name='new_post'),
    url(r'^accounts/mp/$', 
        'posts.views.manage_posts',
        name='manage_posts'),
    url(r'^accounts/ep/(?P<cat_slug>\w{1})/(?P<post_id>\d+)/$', 
        'posts.views.edit_post',
        name='edit_post'),
    url(r'^accounts/ep/success/$', 
        'posts.views.edit_post_success',
        name='edit_post_success'),
    url(r'^accounts/dp/(?P<cat_slug>\w{1})/(?P<post_id>\d+)/$', 
        'posts.views.delete_post',
        name='delete_post'),
    url(r'^accounts/dp/success/$', 
        'posts.views.delete_post_success',
        name='delete_post_success'),
    url(r'^maxquota/$',
        'posts.views.max_posts_exceeded',
        name='max_posts_exceeded'),
)