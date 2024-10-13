from django.contrib import admin
from django.urls import include, path
from debug_toolbar import urls as debug_toolbar_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/cinema/", include("cinema.urls", namespace="cinema")),
    path("__debug__/", include(debug_toolbar_urls)),
]
