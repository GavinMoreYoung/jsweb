from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index),
    url('^list/$', views.list),
    url('^info/$', views.info),
    url('^wz/$',views.wz),
    url('^wzinfo/(\d+)$',views.wzinfo),
    url('^finddy/$',views.finddy),
]
