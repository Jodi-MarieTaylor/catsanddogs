from django.conf.urls import url 
from . import views
from django.contrib import admin

from . import views

urlpatterns = [
   url(r'^$', views.index, name ='index'),
   # ex: /polls/5/
    url(r'^view/cats', views.view_cats, name ='view_cats'),
    url(r'^view/dogs', views.view_dogs, name ='view_dogs'),

    url(r'^add/cats', views.add_cats, name ='add_cats'),
    url(r'^cats/create', views.create_cats, name ='create_cats'),
    url(r'^add/dogs', views.add_dogs, name ='add_dogs'),
    url(r'^dogs/create', views.create_dogs, name ='create_dogs'),
    url(r'^dogs/remove/(?P<dog_id>[0-9]+)', views.delete_dogs, name ='delete_dogs'),
   
    url(r'cats/remove/(?P<cat_id>[0-9]+)', views.delete_cats, name ='delete_cats'),

]
