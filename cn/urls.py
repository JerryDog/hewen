from django.conf.urls import patterns, include, url

from django.contrib import admin
from cn import views
from django.conf.urls.static import static
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hewen.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index, name='index'),
    url(r'^news/(\d*)/$',views.news, name='news'),
    url(r'^news/$',views.newsmain, name='newsmain'),
    url(r'^othernews/$',views.othernews, name='othernews'),
    url(r'^contact/$',views.contact, name='contact'),
    url(r'^hr/$',views.hr, name='hr'),
    url(r'^service/$',views.service, name='service'),
    url(r'^release/$',views.release, name='release'),
    url(r'^bookprod/$',views.bookprodmain, name='bookprodmain'),
    url(r'^partners/$',views.partners, name='partners'),
    url(r'^bookservice/$',views.bookservice, name='bookservice'),
    url(r'^hewentong/$',views.hewentong, name='hewentong'),
    url(r'^hwtprod/$',views.hwtprod, name='hwtprod'),
    url(r'^hwtsoftware/$',views.hwtsoftware, name='hwtsoftware'),
    url(r'^hwtsource/$',views.hwtsource, name='hwtsource'),
    url(r'^about/(\d*)/$',views.about, name='about'),
    url(r'^about/$',views.aboutmain, name='aboutmain'),
    url(r'^bookprod/(\d*)/$',views.bookprod, name='bookprod'),
    url(r'^vedio/(\d*)/$',views.vedio, name='vedio'),
)+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
