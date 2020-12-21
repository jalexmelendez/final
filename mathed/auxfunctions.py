from django.http import HttpResponse, JsonResponse
from .models import user, achieve, test, school, school_group
#Auxiliar functions

##Http Responses

def badHttpRequest():
    return HttpResponse('<H1>400 BAD REQUEST</h1><br><h3>Invalid request method.</h3>')

def dbProcessFailure():
    return HttpResponse('<H1>Bad database request.</h2>')

def dbProcessFailureUsr_exist():
    return HttpResponse('<H1>This username already exist.</h1>')

##Authentication functions

def handleSessionException(request):
    try:
        if request.session.get('is_authenticated') is True:
            return True
        else:
            return False
    except:
        return False

## User information queries

class userData:

    def __init__(self):
        pass

    @staticmethod
    def basic(request):
        user = request.session.get('user')
        is_supervisor = request.session.get('is_supervisor')
        data = {
            'user': user,
            'is_supervisor': is_supervisor
        }
        return data
    
    @staticmethod
    def profile(request):
        db_extract = user.objects.filter(username=request.session.get('user')).first()
        data = {
            'user': db_extract.username,
            'first_name': db_extract.first_name,
            'last_name': db_extract.last_name,
            'age': db_extract.age,
            'profile_pic': db_extract.profile_pic,
            'mail': db_extract.mail,
            'phone': db_extract.phone,
            'score': db_extract.score,
        }
        return data
    
    @staticmethod
    def progress(request):
        db_extract = user.objects.filter(username=request.session.get('user')).first()
        data = {
            'current_lesson': db_extract.current_lesson,
            'difficulty_load': db_extract.difficulty_load,
            'score': db_extract.score,
            'avg_1': db_extract.avg_1,
            'avg_2': db_extract.avg_2,
            'avg_3': db_extract.avg_3,
            'avg_4': db_extract.avg_4
        }
        return data


class userDataPost:

    def __init__(self):
        pass

    @staticmethod
    def updateProfile(userDataJson):
        user_data = user.objects.filter(username=userDataJson['user']).first()
        user_data.first_name = userDataJson['first_name']
        user_data.last_name = userDataJson['last_name']
        user_data.age = userDataJson['age']
        user_data.profile_pic = userDataJson['profile_pic']
        user_data.mail = userDataJson['mail']
        user_data.phone = userDataJson['phone']
        user_data.save()
        return 0

class apiRoutes:

    def __init__(self):
        pass

    @staticmethod
    def achievements(data):
        try:
            db_extract = achieve.objects.filter(username=data).first()
            response = {
                'user': db_extract.username,
                '1': db_extract.a1,
                '2': db_extract.a2,
                '3': db_extract.a3,
                '4': db_extract.a4,
                '5': db_extract.a5,
                '6': db_extract.a6,
                '7': db_extract.a7,
                '8': db_extract.a8,
                '9': db_extract.a9,
                '10': db_extract.a10,
                }
            return response
        except:
            achieveEngine.newAchieve(data)

##test engine

##User average

##Achievement engine

class achieveEngine:

    def __init__(self):
        pass

    @staticmethod
    def newAchieve(data):
        newAchieve = achieve.objects.create(username=data)
        newAchieve.save()
        apiRoutes.achievements(data)

##Global data calculation
###All users
###All schools
###All Groups

##Query to JSON array engine