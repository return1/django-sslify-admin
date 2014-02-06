from django.conf.urls import include, url
from django.conf.urls import patterns
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin_custom_namespace/', include(admin.site.urls)),
)
