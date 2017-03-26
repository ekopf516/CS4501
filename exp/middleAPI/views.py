from django.shortcuts import render
import urllib.request
import urllib.parse
import json
from django.http import JsonResponse
import datetime
from datetime import datetime as dtime
from . import forms
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect

def allBooks(request):
    if (request.method == "GET"):
        req = urllib.request.Request('http://models-api:8000/book_display/')
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        resp = json.loads(resp_json)
        books = resp['resp']['match']
        booklist = []
        for b in books:
            booklist.append(b)
        book_dict = {'match': booklist}
        return JsonResponse({'status': True, 'resp': book_dict})

    return JsonResponse({'status': False, 'resp': 'URL only handles GET requests'})


def userInfo(request, user_id):
    if(request.method == "GET"):
        req = urllib.request.Request('http://models-api:8000/user_display/' + user_id + '/')
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        return JsonResponse({'status': True, 'resp': json.loads(resp_json)})

    return JsonResponse({'status': False, 'resp': 'URL only handles GET requests'})

def bookInfo(request, book_id):
    if (request.method == "GET"):
        req = urllib.request.Request('http://models-api:8000/book_display/' + book_id + '/')
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        return JsonResponse({'status': True, 'resp': json.loads(resp_json)})

    return JsonResponse({'status': False, 'resp': 'URL only handles GET requests'})

def homepage(request):
    if (request.method == "GET"):

        # New Releases
        req = urllib.request.Request('http://models-api:8000/recently_published/')
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        resp = json.loads(resp_json)
        books = resp['resp']['match']
        titles = []
        ids = []
        for b in books:
            titles.append(b['title'])
            ids.append(b['id'])
        new = {'titles': titles, 'ids': ids}

        # All books
        req = urllib.request.Request('http://models-api:8000/book_display/')
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        resp = json.loads(resp_json)
        books = resp['resp']['match']
        titles = []
        ids = []
        for b in books:
            titles.append(b['title'])
            ids.append(b['id'])
        all = {'titles': titles, 'ids': ids}

        home = {'new': new, 'all': all}

        return JsonResponse({'status': True, 'resp': home})

    return JsonResponse({'status': False, 'resp': 'URL only handles GET requests'})

def login(request):
    if(request.method == 'POST'):
        f = forms.login_form(request.POST)
        if (f.is_valid()):
            username = f.cleaned_data['user_name']
            password = f.cleaned_data['password']
            post_data = {'user_name': username, 'password': password, 'last_name': 'a', 'first_name': 'b'}
            post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
            req = urllib.request.Request(url='http://models-api:8000/login/', data=post_encoded, method='POST')
            resp_json = urllib.request.urlopen(req).read().decode('utf-8')
            resp = json.loads(resp_json)
            return JsonResponse({'status': True, 'resp': resp})
        else: return JsonResponse({'status': False, 'resp': 'invalid input'})
    return JsonResponse({'status': False, 'resp': 'URL only handles POST requests'})

def create_user(request):
    if(request.method == 'POST'):
        f = forms.user_info(request.POST)
        if (f.is_valid()):
            username = f.cleaned_data['user_name']
            password = f.cleaned_data['password']
            lastname = f.cleaned_data['last_name']
            firstname = f.cleaned_data['first_name']
            post_data = {'user_name': username, 'password': password, 'last_name': lastname, 'first_name': firstname}
            post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
            req = urllib.request.Request(url='http://models-api:8000/createUser/', data=post_encoded, method='POST')
            resp_json = urllib.request.urlopen(req).read().decode('utf-8')
            resp = json.loads(resp_json)
            return JsonResponse({'status': True, 'resp': resp})
        else: return JsonResponse({'status': False, 'resp': 'invalid input'})
    return JsonResponse({'status': False, 'resp': 'URL only handles POST requests'})

def fetch_user_name(request):
    if(request.method == 'POST'):
        f = forms.authenticate_form(request.POST)
        if(f.is_valid()):
            authenticator = f.cleaned_data['authenticator']
            post_data = {'authenticator': authenticator}
            post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
            req = urllib.request.Request('http://models-api:8000/authenticate/', data=post_encoded, method='POST')
            resp_json = urllib.request.urlopen(req).read().decode('utf-8')
            resp = json.loads(resp_json)
            return JsonResponse({'status': True, 'resp': resp})
        else: return JsonResponse({'status': False, 'resp': 'invalid input'})
    return JsonResponse({'status': False, 'resp': 'URL only handles POST requests'})


def logout(request):
    if(request.method == 'POST'):
        f = forms.authenticate_form(request.POST)
        if(f.is_valid()):
            authenticator = f.cleaned_data['authenticator']
            post_data = {'authenticator': authenticator}
            post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
            req = urllib.request.Request('http://models-api:8000/logout/', data=post_encoded, method='POST')
            resp_json = urllib.request.urlopen(req).read().decode('utf-8')
            resp = json.loads(resp_json)
            return JsonResponse({'status': True, 'resp': resp})
        else: return JsonResponse({'status': False, 'resp': 'invalid input'})
    return JsonResponse({'status': False, 'resp': 'URL only handles POST requests'})
