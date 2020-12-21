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
from .models import user, achieve, test, school, school_group
from .auxfunctions import badHttpRequest, dbProcessFailure, dbProcessFailureUsr_exist, handleSessionException, userData, userDataPost, apiRoutes
from .sessionmaker import createUser, userLogin

# Create your views here.

def index(request):
    return render(request, 'index.html')

def login(request):
    try:
        if request.session.is_authenticated is True:
            return HttpResponseRedirect(reverse('profile'))
    except:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            req = userLogin(username, password, request)
            if req is False:
                message = {
                    'error': "Wrong password or invalid username."
                    }
                return render(request, 'error.html', message)
            else:
                request = req
                return HttpResponseRedirect(reverse('profile'), request)
        else:
            return HttpResponse(badHttpRequest())

def create(request):
    if request.method == 'POST':
        username = request.POST['username']
        mail = request.POST['email']
        password = request.POST['password']
        create = createUser(username, mail, password)
        if create is False:
            return HttpResponse(dbProcessFailureUsr_exist())
        else:
            return JsonResponse(create, safe=False)
    else:
        return HttpResponse(badHttpRequest())

def logout(request):
    try:
        del request.session['user']
        del request.session['is_supervisor']
        del request.session['is_authenticated']
        return HttpResponseRedirect(reverse('index'))
    except KeyError:
        pass
    return HttpResponseRedirect(reverse('index'))

def profile(request):
    authenticated = handleSessionException(request)
    if authenticated is True:
        user_info = userData.profile(request)
        if request.method == 'POST':
            userDataJson = {
                'user': request.session.get('user'),
                'first_name': request.POST['first_name'],
                'last_name': request.POST['last_name'],
                'age': request.POST['age'],
                'profile_pic': request.POST['profile_pic'],
                'mail': request.POST['mail'],
                'phone': request.POST['phone']
            }
            userDataPost.updateProfile(userDataJson)
            return HttpResponseRedirect(reverse('profile'), request)
        else:
            return render(request, 'dash_main.html', user_info)
    else:
        return HttpResponseRedirect(reverse('index'))

def controller(request):
    key = handleSessionException(request)
    if key == True:
        data = json.loads(request.body)
        #data = {'option': 'achievements', 'user': 'alex'}
        if request.method == 'PUT':
            return HttpResponseRedirect(reverse('profile'))
        elif request.method == 'POST':
            apiRouter = {
                'achievements': apiRoutes.achievements(data['user']),
                }
            operation = apiRouter.get(data['option'])
            return JsonResponse(operation, safe=False)
        else:
            error = {'Error': 'invalid method'}
            return JsonResponse(error)
    else:
        error = {'Error': 'Invalid api key'}
        return JsonResponse(error)