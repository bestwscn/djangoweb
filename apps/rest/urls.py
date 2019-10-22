from django.urls import path, include
from djangoweb.router import router


urlpatterns = [
    path('auth/', include('rest_framework.urls')),
]