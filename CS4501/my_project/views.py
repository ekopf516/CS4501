from django.http import JsonResponse
from .forms import UserForm, BookForm, authenticate_form
from django.forms import model_to_dict
from .models import user, book, Authenticator, recomendation
from datetime import datetime as dtime
import datetime
from django.utils import timezone
from django.shortcuts import render, HttpResponse
import os
import hmac
from project1 import settings
from django.contrib.auth import hashers
from django.views.decorators.csrf import csrf_protect
import json

def allUsers(request):
    if (request.method == "GET"):
        userlist = []
        for u in user.objects.all():
            u_dict = model_to_dict(u, exclude=['bag'])
            userlist.append(u_dict)
        user_dict = {'match': userlist}
        return JsonResponse({'status': True, 'resp': user_dict})

    return JsonResponse({'status': False, 'resp': 'URL only handles GET requests'})


def allBooks(request):
    if (request.method == "GET"):
        booklist = []
        for b in book.objects.all():
            b_dict = model_to_dict(b)
            booklist.append(b_dict)
        book_dict = {'match': booklist}
        return JsonResponse({'status': True, 'resp': book_dict})

    return JsonResponse({'status': False, 'resp': 'URL only handles GET requests'})

def recentlyPublished(request):
    if (request.method == "GET"):
        booklist = []
        for b in book.objects.all():
            #dtime.strptime(b.pub_date, "%Y-%m-%dT%H:%M:%SZ")
            if(b.pub_date >= datetime.date(day=1,month=1,year=2016)):
                booklist.append(model_to_dict(b))
        book_dict = {'match': booklist}
        return JsonResponse({'status': True, 'resp': book_dict})

    return JsonResponse({'status': False, 'resp': 'URL only handles GET requests'})


def viewUser(request, user_id):
    if user.objects.filter(id=user_id):
        theUser = user.objects.get(pk=user_id)
    else:
        return JsonResponse({'status': False, 'message': "No user was found with that ID", 'data': None})
    #Display User
    if(request.method == "GET"):
        if user.objects.filter(id=user_id):
            user_dict = model_to_dict(theUser, exclude=['bag'])
            return JsonResponse({'status': True, 'resp': user_dict})
    # Edit User
    # talk to TA about how to have no required fields for this
    elif(request.method == "POST"):
        form = UserForm(request.POST, instance=theUser)
        if (form.is_valid()):
            form.save()
            theUser = user.objects.get(pk=user_id)
            user_dict = model_to_dict(theUser, exclude=['bag'])
            return JsonResponse({'status': True, 'resp': user_dict})
        else:
            return JsonResponse({'status': False, 'resp': 'invalid input'})

    return JsonResponse({'status': False, 'resp': 'URL only handles GET and POST requests'})


def viewBook(request, book_id):
    if book.objects.filter(id=book_id):
        theBook = book.objects.get(pk=book_id)
    else:
        return JsonResponse({'status': False, 'message': "No book was found with that ID", 'data': None})
    # Display Book
    if (request.method == "GET"):
        if book.objects.filter(id=book_id):
            book_dict = model_to_dict(theBook)
            return JsonResponse({'status': True, 'resp': book_dict})
    # Edit Book
    # talk to TA about how to have no required fields for this
    elif (request.method == "POST"):
        form = BookForm(request.POST, instance=theBook)
        if (form.is_valid()):
            form.save()
            theBook = book.objects.get(pk=book_id)
            book_dict = model_to_dict(theBook)
            return JsonResponse({'status': True, 'resp': book_dict})
        else:
            return JsonResponse({'status': False, 'resp': 'invalid input'})

    return JsonResponse({'status': False, 'resp': 'URL only handles GET and POST requests'})

def getRecommendations(request, book_id):
    if not book.objects.filter(id=book_id):
        return JsonResponse({'status': False, 'message': "No book was found with that ID", 'data': None})
    if recomendation.objects.filter(book_id = book_id):
        recoList = recomendation.objects.get(book_id =book_id).recommendations
    else:
        return JsonResponse({'status': False, 'message': "No recommendations found", 'data': None})
    recoList = recoList.split(",")
    bookList = []
    del recoList[-1]
    for b in recoList:
        if(b != ""):
            b = int(b)
            if (book.objects.filter(pk = b)):
                bookList.append((b, book.objects.get(pk = b).title))
    return JsonResponse({'status': True, 'resp': bookList})


def createUser(request):
    if request.method == "POST":
        form = UserForm(data=request.POST)
        if(form.is_valid()):
            for u in user.objects.all():
                if(form.cleaned_data['user_name'] == u.user_name):
                    return JsonResponse({'status': False, 'resp': 'user already exists'})
            u = user(user_name=form.cleaned_data['user_name'],
                     first_name=form.cleaned_data['first_name'],
                     last_name=form.cleaned_data['last_name'],
                     password=hashers.make_password(form.cleaned_data['password']))
            u.save()
            return login(request)
        else: return JsonResponse({'status': False, 'resp': 'invalid input'})
    return JsonResponse({'status' : False, 'resp': 'This URL only handles POST requests'})

def createBook(request):
    if request.method == "POST":
        form = BookForm(data=request.POST)
        if(form.is_valid()):
            f = form.save()
            return JsonResponse({'status': True, 'resp' : 'book has been created.', 'pk': f.pk})
        else: return JsonResponse({'status': False, 'resp': 'models layer form did not validate'})
    return JsonResponse({'status' : False, 'resp': 'This URL only handles POST requests'})


def removeUser(request, user_id):
    if user.objects.filter(id = user_id):
        theUser = user.objects.get(pk = user_id)
        theUser.delete()
        return JsonResponse({'status': True, 'resp': 'User Deleted'}, safe = False)
    else:
        return JsonResponse({'status': False, 'resp': 'User Not Found'}, safe = False)


def removeBook(request, book_id):
    if book.objects.filter(id = book_id):
        theBook = book.objects.get(pk = book_id)
        theBook.delete()
        return JsonResponse({'status': True, 'resp': 'Book Deleted'}, safe = False)
    else:
        return JsonResponse({'status': False, 'resp': 'Book Not Found'}, safe = False)

#@csrf_protect
def login(request):
    if request.method == "POST":
        form = UserForm(data=request.POST)
        nouser = True
        if(form.is_valid()):
            for u in user.objects.all():
                if (u.user_name == form.cleaned_data['user_name']):
                    theuser = u
                    nouser = False
            if nouser:
                return JsonResponse({'status': False, 'resp': 'invalid user info'})

            if (hashers.check_password(form.cleaned_data['password'], theuser.password)):
                unique = True
                while (unique):
                    authenticator = hmac.new(
                        key=settings.SECRET_KEY.encode('utf-8'),
                        msg=os.urandom(32),
                        digestmod='sha256',
                    ).hexdigest()
                    unique = False
                    for a in Authenticator.objects.all():
                        if (a == authenticator): unique = True
                auth = Authenticator(authenticator=authenticator, user_id=theuser.pk)
                auth.save()
                auth_dict = model_to_dict(auth)
                return JsonResponse({'status': True, 'resp': auth_dict})
            else:
                return JsonResponse({'status': False, 'resp': 'invalid user info'})
    return JsonResponse({'status' : False, 'resp': 'This URL only handles POST requests'})

def authenticate(request):
    if request.method == "POST":
        form = authenticate_form(data=request.POST)
        noauth = True
        if(form.is_valid()):
            for a in Authenticator.objects.all():
                if(a.date_created < (timezone.now()-datetime.timedelta(1))):
                    a.delete()
            for a in Authenticator.objects.all():
                if (a.authenticator == form.cleaned_data['authenticator']):
                    auth = a
                    noauth = False
            if noauth:
                return JsonResponse({'status': False, 'resp': 'user not authorized'})

            for u in user.objects.all():
                if (auth.user_id == u.pk):
                    user_name = u.user_name

            return JsonResponse({'status': True, 'resp': {'user_name': user_name}})
        else: return JsonResponse({'status': False, 'resp': 'invalid user info'})
    return JsonResponse({'status' : False, 'resp': 'This URL only handles POST requests'})

def logout(request):
    if request.method == "POST":
        form = authenticate_form(data=request.POST)
        if(form.is_valid()):
            for a in Authenticator.objects.all():
                if (a.authenticator == form.cleaned_data['authenticator']):
                    a.delete()
                    return JsonResponse({'status': True, 'resp': 'user logged out'})
        else: return JsonResponse({'status': False, 'resp': 'invalid user info'})
    return JsonResponse({'status' : False, 'resp': 'This URL only handles POST requests'})


