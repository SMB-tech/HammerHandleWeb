"""HammerHandleWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from HammerHandleWeb.views import main
from HammerHandleWeb.views.army_creation import main as army_creation_main

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', main.index, name='root'),
    url(r'^index.htm', main.index, name='home'),
    url(r'^army_creation/main.html', army_creation_main.index, name='army_creation_main'),

    #Languages
    url(r'^i18n/', include('django.conf.urls.i18n')),
]
