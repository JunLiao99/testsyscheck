"""board URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from boardapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.login),
    url(r'^getq/$', views.getjsonq),
    url(r'^getid/$', views.getjsonid),
    url(r'^index/$', views.index),
    url(r'^index/(\w+)/$', views.index),
    # url(r'^post/$', views.post),
    url(r'^login/$', views.login),
    url(r'^change/$', views.change),
    url(r'^serch/$', views.serch),
    url(r'^logout/$', views.logout),
    url(r'^adminmain/$', views.adminmain),
    url(r'^adminmain/(\w+)/$', views.adminmain),
    url(r'^delete/(\d+)/$', views.delete),
    url(r'^delete/(\d+)/(\w+)/$', views.delete),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^admin/', admin.site.urls),
] + static(settings.STATIC_URL,doucment_root = settings.STATIC_URL)
