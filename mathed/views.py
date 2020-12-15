import datetime
import json

#from django.contrib.auth import authenticate, login, logout
#from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
#from rest_framework import viewsets
#from rest_framework import permissions
#from .serializers import UserSerializer, PostSerializer
#from django.views.decorators.csrf import csrf_protect, csrf_exempt

#from .models import

# Create your views here.

def index(request):
    return HttpResponse('hello')