from django.http import HttpResponse
from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render,render_to_response, redirect
from django.utils import timezone
from django.db.models import F
import json
import datetime
from .forms import CatsForm, DogsForm, OwnersForm


from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
#from birthdayreminder.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Cats, Dogs, Owner

def index(request):
    return HttpResponse("Hello, world.")
    
def view_cats(request):
    cats = Cats.objects.all()

    return  render(request, 'admincatsanddogs/cats/all.html', {'cats':cats})
def view_dogs(request):
    dogs= Dogs.objects.all()

    return  render(request, 'admincatsanddogs/dogs/all.html', {'dogs': dogs})


def add_cats(request):
    form =  CatsForm()
    return  render(request, 'admincatsanddogs/addpets.html', {'form': form})
def add_dogs(request):
    form =  DogsForm()
    return  render(request, 'admincatsanddogs/adddogs.html', {'form': form})
    
def create_cats(request):
     if request.method == 'POST':
        print("Method is post")
        # create a form instance and populate it with data from the request:
        form = CatsForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            cats = form.save(commit=False)
            cats.owner = Owner.objects.get(pk=1)
            cats.save()
     allcats = Cats.objects.all()

     return  render(request, 'admincatsanddogs/cats/all.html', {'cats': allcats})


    
def create_dogs(request):
     if request.method == 'POST':
        print("Method is post")
        # create a form instance and populate it with data from the request:
        form = DogsForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            dogs = form.save(commit=False)
            dogs.owner = Owner.objects.get(pk=1)

            dogs.save()
     alldogs = Dogs.objects.all()

     return  render(request, 'admincatsanddogs/dogs/all.html', {'dogs': alldogs})
     
def delete_cats(request,cat_id):

    cat = Cats.objects.get(id= cat_id)
    cat.delete()
    return redirect('/pets/view/cats')


def delete_dogs(request, dog_id):
    dog = Dogs.objects.get(id=dog_id)

    dog.delete()
    return redirect('/pets/view/dogs')


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
    
