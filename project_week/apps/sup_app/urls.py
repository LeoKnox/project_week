from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^create$', views.create),
    url(r'^create_weapon$', views.create_weapon),
    url(r'^create_spell$', views.create_spell),
    url(r'^main$', views.main),
    url(r'^test$', views.test),
    url(r'^combat$', views.combat),
]