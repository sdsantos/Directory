from django.conf import settings
from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # (r'^yoursite/', include('yoursite.foo.urls')),
	# (r'^admin/doc/', include('django.contrib.admindocs.urls')), 
	# And add 'django.contrib.admindocs' to INSTALLED_APPS
    
    (r'^admin/(.*)', admin.site.root),
	(r'^submit', 'directory.views.submit'),
    (r'^media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
	url(r'^$', 'directory.views.index', name='index'),
)

urlpatterns += patterns('',
    url(r'^captcha/', include('captcha.urls')),
)