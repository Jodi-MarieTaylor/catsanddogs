from django.http import HttpResponse
from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render,render_to_response, redirect
from django.utils import timezone
from django.db.models import F
import json
import datetime


from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
#from birthdayreminder.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
    
def view_cats(request):
    return  render(request, 'pets/view/cats.html')
    
def add_pets(re
    
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)