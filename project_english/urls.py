from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app_english.urls')),
    path('accounts/',include('user_app.urls')),
]
