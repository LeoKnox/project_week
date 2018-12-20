from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^battle$', views.battle),
    url(r'^create_monster$', views.create_monster),
]