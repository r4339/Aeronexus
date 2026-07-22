from django.contrib import admin
from django.urls import path, include
handler403 = "config.views.permission_denied"
urlpatterns = [
    path("admin/", admin.site.urls),

    path(
        "accounts/",
        include("accounts.urls")
    ),
    path(
    "assets/",
    include("assets.urls")
),
path("habilitations/", include("habilitations.urls")),
path("audit/", include("audit.urls")),
path("dashboard/", include("dashboard.urls")),
path("access/", include("access.urls")),
path("compliance/", include("compliance.urls")),
path("", include("core.urls")),

]
