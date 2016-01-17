from django.conf.urls import url
from . import views
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from celebidties import settings

import views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # ex: /polls/

    # url(r'^$', 'celebidties.views.index', name='index'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^test/', 'celebidties.views.test'),
    url(r'^pretty/', 'celebidties.views.pretty'),

    # url(r'^test2/', 'celebidties.views.test2'),

    url(r'^test2/', 'celebidties.views.test2'),
    # (r'^articles/(\d{4})/$', 'news.views.year_archive'),
    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    # url(r'^test/', 'celebidties.views.some_view', name='some_view')



    # url(r'^$', 'celebidties.views.index'),
    # url(r'^$', 'celebidties.views.test_draw'),
    # url(r'^polls/', include('polls.urls')),
    # url(r'^admin/', include(admin.site.urls)),
    # url(r'^$', views.index, name='index'),
    # url(r'^$', 'celebidties.views.home', name='home'),
    # url(r'^celebidties/', include('celebidties.foo.urls')),
    # url(r'^rofl/', 'celebidties.views.test_draw'),
    # url(r'^$', 'celebidties.views.test_draw'),
    # url(r'^$', templates.index, name='index'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
