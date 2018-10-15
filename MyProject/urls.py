from django.conf.urls import url, include
from django.contrib import admin
from RssReader.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^RssReader/$',  RssReaderView),
]
