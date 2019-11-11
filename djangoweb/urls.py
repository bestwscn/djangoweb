"""djangoweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from djangoweb.admin import admin
from django.urls import path, include, re_path
from djangoweb.router import router

# admin.site.login = login_required(admin.site.login)
admin.site.site_header = '管理后端'
admin.site.site_title = '管理后端'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.rest.urls')),
    path('accounts/', include('apps.myaccount.urls')),
    path('pages/', include('django.contrib.flatpages.urls')),
]

urlpatterns += [
    re_path(r'^api/', include(router.urls)),
]