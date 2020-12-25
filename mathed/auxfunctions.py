from django.http import HttpResponse, JsonResponse
#from django.db.models import 
from .models import user, achieve, test, school, school_group
from random import randint
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
    
    @staticmethod
    def top_by_score():
        try:
            db_extract = user.objects.order_by('-score')[0:10]
            response = []
            for db_extract in db_extract:
                data_dict = {
                    'username': db_extract.username,
                    'score': db_extract.score,
                    'profile_pic': db_extract.profile_pic,
                    }
                response.append(data_dict)
            return response
        except:
            response = {"ERROR": "An error has occured."}
            return response

##test engine

class testEngine:
    def __init__(self):
        self.testLength = 25
        pass

    @staticmethod
    def rndNumGen():
        testLength = 5
        data = []
        for i in range(0, testLength):
            i += 1
            numStruct = {'1': randint(1, 500), '2': randint(1,500)}
            data.append(numStruct)
        return data

    @staticmethod
    def sum():
        numbers = testEngine.rndNumGen()
        data = []
        for i in range(0, len(numbers)):
            answer = numbers[i]['1'] + numbers[i]['2']
            dstruct = {'1': numbers[i]['1'], '2': numbers[i]['2'], 'ans': hex(answer)}
            data.append(dstruct)
            i += 1
        return data

    @staticmethod
    def sub():
        numbers = testEngine.rndNumGen()
        data = []
        for i in range(0, len(numbers)):
            answer = numbers[i]['1'] - numbers[i]['2']
            dstruct = {'1': numbers[i]['1'], '2': numbers[i]['2'], 'ans': hex(answer)}
            data.append(dstruct)
            i += 1
        return data

    @staticmethod
    def multi():
        numbers = testEngine.rndNumGen()
        data = []
        for i in range(0, len(numbers)):
            answer = numbers[i]['1'] * numbers[i]['2']
            dstruct = {'1': numbers[i]['1'], '2': numbers[i]['2'], 'ans': hex(answer)}
            data.append(dstruct)
            i += 1
        return data

##Test solving engine

class testSolver:

    def __init__(self):
        pass

    @staticmethod
    def evaluator(answers):
        data = []
        score_ponts = 0
        for i in range(0, len(answers['data'])):
            userAns = answers['data'][i]['user']
            correctAns = answers['data'][i]['correct']
            correct = int(correctAns, 16)
            if userAns == correct:
                evaluation = True
                score_ponts += 1
            else:
                evaluation = False
            format = {'user': userAns,'correct': correct, 'evaluation': evaluation}
            data.append(format)
        testSolver.updateScore(answers['user'], score_ponts)
        return data
    
    @staticmethod
    def updateScore(username, points):
        db_extract = user.objects.filter(username=username).first()
        db_extract.score = int(db_extract.score) + points
        db_extract.save()

##Achievement engine

class achieveEngine:

    def __init__(self):
        pass

    @staticmethod
    def newAchieve(data):
        newAchieve = achieve.objects.create(username=data)
        newAchieve.save()
        apiRoutes.achievements(data)

    @staticmethod
    def achievementUnlock(totalScore, testScore):
        if testScore == 5:
            pass
        else:
            return False


class achieveList:

    def __init__(self):
        pass

    @staticmethod
    def one():
        pass

    @staticmethod
    def two():
        pass

    @staticmethod
    def three():
        pass