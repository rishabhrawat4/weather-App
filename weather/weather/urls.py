
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('weather_report.urls')),
    path('admin/', admin.site.urls),
]
