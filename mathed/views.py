import datetime
import json

from django.contrib.auth import authenticate, login, logout
#from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
#from rest_framework import viewsets
#from rest_framework import permissions
#from .serializers import UserSerializer, PostSerializer
#from django.views.decorators.csrf import csrf_protect, csrf_exempt

from .models import user, achieve, test, school, school_group, supervisor

# Create your views here.

def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        data = request.POST['username']
        return HttpResponse(data)