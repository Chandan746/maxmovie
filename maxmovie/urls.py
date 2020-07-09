
from django.contrib import admin
from django.urls import path
from .views import getMaxMovie
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',getMaxMovie),
]
