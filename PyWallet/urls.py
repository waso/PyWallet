from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'engine.views.home', name='home'),
    url(r'^add/$',    'engine.views.add',    name='add'),
    url(r'^remove/$', 'engine.views.remove', name='remove'),
    url(r'^update/$', 'engine.views.update', name='update'),
    url(r'^login/$', 'engine.views.sign_in', name='sign_in'),
    url(r'^logout/$', 'engine.views.sign_out', name='sign_out'),
    # Examples:
    # url(r'^$', 'PyWallet.views.home', name='home'),
    # url(r'^PyWallet/', include('PyWallet.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
