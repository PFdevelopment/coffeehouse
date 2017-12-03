from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<store_id>\d+)/', views.detail, {'location': 'headquarters'}, name='detail'),
    url(r'^(?P<store_id>\d+)/', views.detail, name='detailwithouloc'),
]
