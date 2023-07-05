from django.conf import settings
from django.contrib import admin
from django.contrib.flatpages import views as flatpage_views
from django.urls import include, path, re_path
from django.views.static import serve
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView

from .core import api, views

urlpatterns = [
    # admin
    path("dj-admin/", admin.site.urls),
    # flatpages
    path("terms/", flatpage_views.flatpage, {"url": "/terms/"}, name="terms"),
    # api
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    path("api/token-auth/", api.AuthTokenView.as_view(), name="token-auth"),
    path("api/protected/", api.ProtectedView.as_view(), name="protected"),
    # accounts
    path("accounts/", include("allauth.urls")),
    path("accounts/settings/", views.settings, name="settings"),
    path("accounts/delete-account/", views.delete_account, name="delete-account"),
    # core
    path("", views.index, name="index"),
    path("terms/", views.terms, name="terms"),
    path("feedback/", views.feedback, name="feedback"),
    path("websocket/", views.websocket, name="websocket"),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
        path("__reload__/", include("django_browser_reload.urls")),
        path("silk/", include("silk.urls", namespace="silk")),
        re_path(
            r"^media/(?P<path>.*)$",
            serve,
            {"document_root": settings.MEDIA_ROOT, "show_indexes": True},
        ),
    ] + urlpatterns
