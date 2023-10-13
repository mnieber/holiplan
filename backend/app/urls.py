from django.conf import settings
from django.contrib import admin
from django.urls import include, path

import api.urls
from app.utils.serve_static import serve_static

urlpatterns = [
    path(r"api/", include(api.urls)),
    path(r"admin/", admin.site.urls),
] + ([] + serve_static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
