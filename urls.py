from django.conf import settings
from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

from directory.feeds import CompaniesFeed, AllCompaniesFeed
feeds = {
    'companies': CompaniesFeed,
    settings.EDITOR_FEED_URL: AllCompaniesFeed,
}


urlpatterns = patterns('',
    
    (r'^admin/(.*)', admin.site.root),
    (r'^media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^$', 'directory.views.index', name='index'),
    url(r'^submit', 'directory.views.submit', name='submit-company'),
    url(r'^captcha/', include('captcha.urls')),
    
    (r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed',
        {'feed_dict': feeds}),
)