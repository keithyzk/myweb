from django.conf.urls import include, url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^blog/$', views.blog,name='blog'),
    url(r'^ariticle/(?P<ariticle_id>\d+)$',views.ariticle_page,name='ariticle_page'),
    url(r'^edit/(?P<ariticle_id>\d+)$',views.edit_page, name='edit_page'),
    url(r'^edit/action/',views.edit_action,name='edit_action'),
]
