import django
from django.contrib import admin


if django.VERSION[:2] < (1, 10):
    from django.conf.urls import patterns, include

    admin.autodiscover()

    urlpatterns = patterns('', (r'^admin/', include(admin.site.urls)))
else:
    from django.conf.urls import url

    urlpatterns = [
        url(r'^admin/', admin.site.urls),
    ]
