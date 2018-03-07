# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # (r'^helloworld/', include('helloworld.foo.urls')),
    #(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    #(r'^admin/', include(admin.site.urls)),

    # Hello, world!
    (r'', 'helloworld.views.index'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),
    )

