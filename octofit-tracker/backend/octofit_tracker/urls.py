from django.contrib import admin
from django.urls import path
from django.http import HttpResponse


def index(request):
    return HttpResponse("OctoFit Tracker backend is running.")


urlpatterns = [
    path("", index),
    path("admin/", admin.site.urls),
]
