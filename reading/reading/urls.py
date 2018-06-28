"""reading URL Configuration

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

from rest_framework import routers
from rest_framework.documentation import include_docs_urls

from book.api import StoryViewSet
from .custom_site import custom_site
from book.views import IndexView, CategoryView, BookView


router = routers.DefaultRouter()
router.register(r'story', StoryViewSet)


urlpatterns = [
    url('^$', IndexView.as_view(), name='index'),
    url('^category/(?P<category_id>\d+).html$', CategoryView.as_view(), name='category'),
    url('book/(?P<pk>\d+).html$', BookView.as_view(), name='detail'),
    url(r'^admin/', admin.site.urls),
    url(r'^cus_admin/', custom_site.urls),
    url(r'api/', include(router.urls)),
    url(r'^api/docs/', include_docs_urls(title='My Book API')),
]
