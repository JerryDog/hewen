from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hewen.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^cn/', include('cn.urls',namespace='cn')),
    url(r'^$', include('cn.urls',namespace='cn')),
)+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
