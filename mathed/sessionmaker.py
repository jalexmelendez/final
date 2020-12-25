import json
import datetime

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import user, achieve, test, school, school_group

def userLogin(username, password, request):
    try:
        username = user.objects.get(username=username, password=password)
        json_data =  ({
            'user': username.username,
            'is_supervisor': username.is_supervisor,
            'is_authenticated': True
            })
        request.session['user'] = json_data['user']
        request.session['is_supervisor'] = json_data['is_supervisor']
        request.session['is_authenticated'] = True
        request.session.modified = True
        return request
    except user.DoesNotExist:
        return False

def createUser(username, mail, password):
    try:
        userexist = user.objects.get(username=username)
        return False
    except user.DoesNotExist:
        usercreate = user.objects.create(username=username, mail=mail, password=password, score=0)
        usercreate.save()
        return True

