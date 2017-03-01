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

def recentlyPublished(request):
    if (request.method == "GET"):
        req = urllib.request.Request('http://exp-api:8000/book_display/')
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        resp = json.loads(resp_json)
        books = resp['resp']['match']
        titles = []
        ids = []
        for b in books:
            titles.append(b['title'])
            ids.append(b['id'])
        combined = zip(titles, ids)
        return render(request, 'index.html', {'NewReleases': combined})
    return HttpResponse("There are no recently published books.")

def bookView(request, book_id):
    if (request.method == "GET"):
        req = urllib.request.Request('http://exp-api:8000/book_display/' + book_id + '/')
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        resp = json.loads(resp_json)
        resp = resp['resp']['resp']
        # return JsonResponse({'status': True, 'resp': resp})
        return render(request, 'book.html', resp)