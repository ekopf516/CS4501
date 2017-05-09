from django.shortcuts import render
import urllib.request
import json
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from . import forms
from http import cookiejar


def homePage(request):
    if (request.method == "GET"):
        #check if authenticated
        username = authenticate(request)

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
        username = authenticate(request)
        user_data = {'username': username}
        encoded = urllib.parse.urlencode(user_data).encode('utf-8')
        req = urllib.request.Request('http://exp-api:8000/book_display/' + book_id + '/', data=encoded)
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        resp = json.loads(resp_json)
        if (resp['resp']['status'] == False):
            return render(request, 'noBook.html')
        resp = resp['resp']['resp']
        resp['username'] = username
        # return JsonResponse({'status': True, 'resp': resp})
        return render(request, 'book.html', resp)

def login(request):
    # If we received a GET request instead of a POST request
    username = authenticate(request)

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
      return render(request, 'login.html', {'message': 'invalid input', 'form': form})

    # Sanitize username and password fields
    username = f.cleaned_data['user_name']
    password = f.cleaned_data['password']

    # Send validated information to our experience layer
    post_data = {'user_name': username, 'password': password, 'last_name': 'a', 'first_name': 'b'}
    post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
    req = urllib.request.Request('http://exp-api:8000/login/', data=post_encoded, method='POST')
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    resp = json.loads(resp_json)

    #Check if the experience layer said they gave us incorrect information
    if (not resp['resp']['status']):
      # Couldn't log them in, send them back to login page with error
      form = forms.login_form()
      return render(request, 'login.html', {'message': 'username or password is incorrect', 'form': form})

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
    username = authenticate(request)

    if (request.COOKIES.get('auth', False) and request.method == 'GET' and username):
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

    username = f.cleaned_data['user_name']
    password = f.cleaned_data['password']
    lastname = f.cleaned_data['last_name']
    firstname = f.cleaned_data['first_name']

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

    authenticator = resp['resp']['resp']['authenticator']

    response = HttpResponseRedirect('http://localhost:8000/home/')
    response.set_cookie("auth", authenticator)

    return response


def create_book_listing(request):
    username = authenticate(request)

    if(not username): return render(request, 'create_book_listing.html', {'message': "you must be logged in to create a lisiting", 'username': username,})

    if request.method == 'GET':
        form = forms.book_info()
        return render(request, 'create_book_listing.html', {'form': form, 'username':username})

    f = forms.book_info(request.POST)

    # Check if the form instance is invalid
    if not f.is_valid():
        # Form was bad -- send them back to login page and show them an error
        form = forms.book_info()
        return render(request, 'create_book_listing.html', {'message': 'invalid input', 'form': form, 'username': username})

    title = f.cleaned_data['title']
    author = f.cleaned_data['author']
    publisher = f.cleaned_data['publisher']
    price = f.cleaned_data['price']
    isbn = f.cleaned_data['isbn_num']
    pub_date = f.cleaned_data['pub_date']

    post_data = {'title': title, 'author': author, 'publisher': publisher, 'price': price, 'isbn_num': isbn, 'pub_date':pub_date}
    post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
    req = urllib.request.Request('http://exp-api:8000/create_book_listing/', data=post_encoded, method='POST')
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    resp = json.loads(resp_json)

    if (not resp['status']):
        form = forms.book_info()
        return render(request, 'create_book_listing.html', {'message': resp['resp'], 'form': form, 'username': username})

    if (not resp['resp']['status']):
        form = forms.book_info()
        return render(request, 'create_book_listing.html', {'message': resp['resp']['resp'], 'form': form, 'username':username})

    return HttpResponseRedirect('http://localhost:8000/home/')


def search(request):
    #figure out how to get shit from the search bar
    username = authenticate(request)

    if(request.method == 'POST'):
        post_data = {'searchquery': request.POST['searchquery']}
        post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
        req = urllib.request.Request('http://exp-api:8000/search/', data=post_encoded, method='POST')
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        resp = json.loads(resp_json)
        if(resp['status']):
            titles = []
            ids = []
            for item in resp['resp']:
                titles.append(item['_source']['title'])
                ids.append(item['_source']['id'])
            all = zip(titles, ids)
            return render(request, 'search.html', {'AllBooks': all, 'username': username})
        else:
            return render(request, 'search.html', {'message': resp['resp'], 'username': username})

    else: return render(request, 'search.html', {'message': 'please search something'})





def authenticate(request):
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

    return username


