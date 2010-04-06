from django.conf import settings
from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # (r'^yoursite/', include('yoursite.foo.urls')),
	# (r'^admin/doc/', include('django.contrib.admindocs.urls')), 
	# And add 'django.contrib.admindocs' to INSTALLED_APPS
    
    (r'^admin/(.*)', admin.site.root),
    (r'^media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
	(r'^$', 'django.views.generic.simple.redirect_to', {'url':'/admin/'})
)
