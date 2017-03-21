from django.shortcuts import render
import urllib.request
import json
from django.http import HttpResponse, JsonResponse

# Create your views here.
# def index(request):
#     req = urllib.request.Request('http://localhost:8001/user_display/')
#     resp_json = urllib.request.urlopen(req).read().decode('utf-8')
#     resp = json.loads(resp_json)
#     return render(request, 'index.html',)

def homePage(request):
    if (request.method == "GET"):

        req = urllib.request.Request('http://exp-api:8000/home_page/')
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        resp = json.loads(resp_json)

        titles = resp['resp']['new']['titles']
        ids = resp['resp']['new']['ids']
        new = zip(titles, ids)

        titles = resp['resp']['all']['titles']
        ids = resp['resp']['all']['ids']
        all = zip(titles, ids)


        return render(request, 'index.html', {'NewReleases':  new, 'AllBooks': all})
    return HttpResponse("There are no recently published books.")

def bookView(request, book_id):
    if (request.method == "GET"):
        req = urllib.request.Request('http://exp-api:8000/book_display/' + book_id + '/')
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        resp = json.loads(resp_json)
        resp = resp['resp']['resp']
        # return JsonResponse({'status': True, 'resp': resp})
        return render(request, 'book.html', resp)