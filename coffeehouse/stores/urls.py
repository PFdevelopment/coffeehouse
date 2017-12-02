from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.detail),
    url(r'^(?P<store_id>\d+)/', views.detail, {'location': 'headquarters'}),
    url(r'^(?P<store_id>\d+)/', views.detail),
]
