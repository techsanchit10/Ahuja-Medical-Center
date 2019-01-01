from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.test_list, name='test_list'),
    url(r'^(?P<package_slug>[-\w]+)/$', views.test_list, name='test_list_by_package'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.test_detail, name='test_detail'),
]
