from django.contrib import admin
from django.urls import path
from django.urls import include

from .views import IndexPage

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", IndexPage.as_view(), name="index"),
    path("cruceros/", include("syl_app.urls")),
]
