from django.contrib import admin
from django.urls import path, include
from .views import index, ConvertView

urlpatterns = [
    path('', index.as_view(), name="index"),
    path('convert/', ConvertView.as_view(), name="convert")
]

