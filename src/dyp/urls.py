from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'joins.views.home', name='home'),
    url(r'^',include('favicon.urls')),
    url(r'^(?P<ref_id>.*)$',  'joins.views.share', name='share'),
    #url(r'^home2/$', 'joins.views.home2', name='home2'),
    # url(r'^blog/', include('blog.urls')),

    
)
