from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from django.views.generic import TemplateView

# serving media files in development
from django.conf import settings
from django.conf.urls.static import static

from registration.backends.default.views import RegistrationView
from registration.forms import RegistrationFormUniqueEmail

#sitemaps
from sitemaps import CitySitemap, RentPostSitemap, SalePostSitemap, StaticViewSitemap

sitemaps = {
    'city_pages': CitySitemap,
    'rent_posts': RentPostSitemap,
    'sale_posts': SalePostSitemap,
    'static': StaticViewSitemap,
}

urlpatterns = patterns('',
    url(r'^robots\.txt$', TemplateView.as_view(
        template_name='robots.txt', 
        content_type='text/plain')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('locations.urls', namespace="locations")),
    url(r'', include('posts.urls', namespace="posts")),
    url(r'', include('categories.urls', namespace="categories")),
    # django-registration urls
    url(r'^accounts/register/$', 
       RegistrationView.as_view(form_class=RegistrationFormUniqueEmail),
       name='registration_register'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    # default auth views
    url(r'^accounts/login/$', 
        'django.contrib.auth.views.login',
        name="login"),
    url(r'^accounts/logout/$',
        'django.contrib.auth.views.logout',
        name="logout"),
    url(r'^accounts/password/reset/$',
        'django.contrib.auth.views.password_reset',
        name="password_reset"),
    url(r'^accounts/password/reset/done/$',
        'django.contrib.auth.views.password_reset_done',
        name="password_reset_done"),
    url(r'^accounts/password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        'django.contrib.auth.views.password_reset_confirm',
        name="password_reset_confirm"),
    url(r'^accounts/password/reset/complete/$',
        'django.contrib.auth.views.password_reset_complete',
        name="password_reset_complete"),
    # urls for static and information pages
    url(r'^about/$', 'core.views.static_pages', name="about"),
    url(r'^terms/$', 'core.views.static_pages', name="terms"),
    url(r'^safety/$', 'core.views.static_pages', name="safety"),
    url(r'^privacy/$', 'core.views.static_pages', name="privacy"),
    url(r'^contact/$', 'core.views.static_pages', name="contact"),
    url(r'^upgrade/$', 'core.views.static_pages', name="upgrade"),
    # urls for handling sitemaps
    url(r'^sitemap\.xml$', 
        'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': sitemaps}),
    # serving media files in development
) 
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
