from django.shortcuts import render
import urllib.request
import json
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from . import forms
from http import cookiejar

def homePage(request):
    if (request.method == "GET"):
        #check if authenticated
        username = None
        if(request.COOKIES.get('auth', False)):
            authenticator = request.COOKIES['auth']
            post_data = {'authenticator': authenticator}
            post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
            req = urllib.request.Request('http://exp-api:8000/authenticate/', data=post_encoded, method='POST')
            resp_json = urllib.request.urlopen(req).read().decode('utf-8')
            resp = json.loads(resp_json)

            if (resp['resp']['status']):
                username = resp['resp']['resp']['user_name']

        req = urllib.request.Request('http://exp-api:8000/home_page/')
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        resp = json.loads(resp_json)

        titles = resp['resp']['new']['titles']
        ids = resp['resp']['new']['ids']
        new = zip(titles, ids)

        titles = resp['resp']['all']['titles']
        ids = resp['resp']['all']['ids']
        all = zip(titles, ids)

        return render(request, 'index.html', {'NewReleases':  new, 'AllBooks': all, 'username': username})
    return HttpResponse("There are no recently published books.")

def bookView(request, book_id):
    if (request.method == "GET"):
        req = urllib.request.Request('http://exp-api:8000/book_display/' + book_id + '/')
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        resp = json.loads(resp_json)
        if (resp['resp']['status'] == False):
            return render(request, 'noBook.html')
        resp = resp['resp']['resp']
        # return JsonResponse({'status': True, 'resp': resp})
        return render(request, 'book.html', resp)

def login(request):
    # If we received a GET request instead of a POST request
    username = None
    if (request.COOKIES.get('auth', False)):
        authenticator = request.COOKIES['auth']
        post_data = {'authenticator': authenticator}
        post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
        req = urllib.request.Request('http://exp-api:8000/authenticate/', data=post_encoded, method='POST')
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        resp = json.loads(resp_json)

        if (resp['resp']['status']):
            username = resp['resp']['resp']['user_name']

    if request.method == 'GET':
        # display the login form page
        message = ''
        if(username):
            message = "you are already logged in"

        form = forms.login_form()
        return render(request, 'login.html', {'form': form, 'username': username, 'message': message})

    # Creates a new instance of our login_form and gives it our POST data
    f = forms.login_form(request.POST)

    # Check if the form instance is invalid
    if not f.is_valid():
      # Form was bad -- send them back to login page and show them an error
      form = forms.login_form()
      return render(request, 'login.html', {'message': 'invalid input', 'form': form, 'username': username})

    # Sanitize username and password fields
    username = f.cleaned_data['user_name']
    password = f.cleaned_data['password']

    # Send validated information to our experience layer
    post_data = {'user_name': username, 'password': password, 'last_name': 'a', 'firstname': 'b'}
    post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
    req = urllib.request.Request('http://exp-api:8000/login/', data=post_encoded, method='POST')
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    resp = json.loads(resp_json)

    #Check if the experience layer said they gave us incorrect information
    if (not resp['resp']['status']):
      # Couldn't log them in, send them back to login page with error
      form = forms.login_form()
      return render(request, 'login.html', {'message': 'username or password is incorrect', 'form': form, 'username':username})

    #If we made it here, we can log them in.
    # Set their login cookie and redirect to back to wherever they came from
    authenticator = resp['resp']['resp']['authenticator']

    response = HttpResponseRedirect('http://localhost:8000/home/')
    response.set_cookie("auth", authenticator)

    return response

def logout(request):
    if (request.COOKIES.get('auth', False)):
        authenticator = request.COOKIES['auth']
        post_data = {'authenticator': authenticator}
        post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
        req = urllib.request.Request('http://exp-api:8000/logout/', data=post_encoded, method='POST')
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        resp = json.loads(resp_json)

        response = HttpResponseRedirect('http://localhost:8000/home/')
        if (resp['resp']['status']):
            response.delete_cookie('auth')
        return response
    else: return HttpResponseRedirect('http://localhost:8000/login/')

def create_user(request):
    username = None
    if (request.COOKIES.get('auth', False)):
        authenticator = request.COOKIES['auth']
        post_data = {'authenticator': authenticator}
        post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
        req = urllib.request.Request('http://exp-api:8000/authenticate/', data=post_encoded, method='POST')
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        resp = json.loads(resp_json)

        if (resp['resp']['status']):
            username = resp['resp']['resp']['user_name']

    if (request.COOKIES.get('auth', False) and request.method == 'GET'):
        form = forms.user_info()
        return render(request, 'create_user.html', {'message': "you are already logged in are you sure you want to create another account?", 'form': form, 'username': username})

    if request.method == 'GET':
        form = forms.user_info()
        return render(request, 'create_user.html', {'form': form})

    f = forms.user_info(request.POST)

    # Check if the form instance is invalid
    if not f.is_valid():
        # Form was bad -- send them back to login page and show them an error
        form = forms.user_info()
        return render(request, 'create_user.html', {'message': 'invalid input', 'form': form, 'username': username})

    # Sanitize username and password fields
    username = f.cleaned_data['user_name']
    password = f.cleaned_data['password']
    lastname = f.cleaned_data['last_name']
    firstname = f.cleaned_data['first_name']

    # Send validated information to our experience layer
    post_data = {'user_name': username, 'password': password, 'last_name': lastname, 'first_name': firstname}
    post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
    req = urllib.request.Request('http://exp-api:8000/create_user/', data=post_encoded, method='POST')
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    resp = json.loads(resp_json)

    if (not resp['status']):
        form = forms.user_info()
        return render(request, 'create_user.html', {'message': resp['resp'], 'form': form, 'username': username})

    if (not resp['resp']['status']):
        form = forms.user_info()
        return render(request, 'create_user.html', {'message': resp['resp']['resp'], 'form': form, 'username':username})

    # If we made it here, we can log them in.
    # Set their login cookie and redirect to back to wherever they came from
    authenticator = resp['resp']['resp']['authenticator']

    response = HttpResponseRedirect('http://localhost:8000/home/')
    response.set_cookie("auth", authenticator)

    return response


# def create_book_listing(request):