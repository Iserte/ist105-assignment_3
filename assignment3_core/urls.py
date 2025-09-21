from django.contrib import admin
from django.urls import path
from math_operations.views import calculate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', calculate),
]