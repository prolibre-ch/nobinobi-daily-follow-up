# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', include('nobinobi_core.urls', namespace='nobinobi_core')),
    path('', include('nobinobi_staff.urls', namespace='nobinobi_staff')),
    path('', include('nobinobi_child.urls', namespace='nobinobi_child')),
    path('', include('nobinobi_daily_follow_up.urls', namespace='nobinobi_daily_follow_up')),
    path('select2/', include('django_select2.urls')),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [path('admin/', admin.site.urls), ]
