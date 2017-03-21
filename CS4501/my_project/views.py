from django.http import JsonResponse
from .forms import UserForm, BookForm
from django.forms import model_to_dict
from .models import user, book
from datetime import datetime as dtime
import datetime
from django.utils import timezone
from django.shortcuts import render, HttpResponse

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
            if(b.pub_date >= timezone.datetime(day=1,month=1,year=2016)):
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

def createUser(request):
    if request.method == "POST":
        form = UserForm(data=request.POST)
        if(form.is_valid()):
            form.save()
            return JsonResponse({'status': True, 'resp' : 'user has been created.'})
        else: return JsonResponse({'status': False, 'resp': 'invalid input'})
    return JsonResponse({'status' : False, 'resp': 'This URL only handles POST requests'})

def createBook(request):
    if request.method == "POST":
        form = BookForm(data=request.POST)
        if(form.is_valid()):
            form.save()
            return JsonResponse({'status': True, 'resp' : 'book has been created.'})
        else: return JsonResponse({'status': False, 'resp': 'invalid input'})
    return JsonResponse({'status' : False, 'resp': 'This URL only handles POST requests'})


def removeUser(request, user_id):
    if user.objects.filter(id = user_id):
        theUser = user.objects.get(pk = user_id)
        theUser.delete()
        return JsonResponse({'status': True, 'resp': 'User Deleted'}, safe = False)
    else:
        return JsonResponse({'status': False, 'resp': 'User Not Found'}, safe=False)


def removeBook(request, book_id):
    if book.objects.filter(id = book_id):
        theBook = book.objects.get(pk = book_id)
        theBook.delete()
        return JsonResponse({'status': True, 'resp': 'Book Deleted'}, safe = False)
    else:
        return JsonResponse({'status': False, 'resp': 'Book Not Found'}, safe=False)





