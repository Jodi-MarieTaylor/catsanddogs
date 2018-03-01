from django.conf.urls import url 
from . import views
from django.contrib import admin

from . import views

urlpatterns = [
   url(r'^$', views.index, name ='index'),
]
