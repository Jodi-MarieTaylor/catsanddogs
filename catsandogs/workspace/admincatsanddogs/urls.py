from django.conf.urls import url 
from . import views
from django.contrib import admin

from . import views

urlpatterns = [
   url(r'^$', views.index, name ='index'),
   # ex: /polls/5/
    url(r'^view/cats', views.view_cats, name ='view_cats'),
    url(r'^add/cats', views.add_cats, name ='add_cats'),
    url(r'^cats/create', views.create_cats, name ='create_cats'),
    url(r'^add/dogs', views.add_dogs, name ='add_dogs'),
    url(r'^dogs/create', views.create_dogs, name ='create_dogs'),
   

]
