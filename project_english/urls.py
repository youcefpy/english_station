from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from project_english import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app_english.urls')),
    path('accounts/',include('user_app.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)