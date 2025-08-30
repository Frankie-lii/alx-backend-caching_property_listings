#!/usr/bin/env python3
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('properties/', include('properties.urls')),
]

