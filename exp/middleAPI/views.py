from django.shortcuts import render
import urllib.request
import urllib.parse
import json
from django.http import JsonResponse
import datetime
from datetime import datetime as dtime


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

def recentlyPublished(request):
    if (request.method == "GET"):
        req = urllib.request.Request('http://models-api:8000/book_display/')
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        resp = json.loads(resp_json)
        books = resp['resp']['match']
        booklist = []
        for b in books:
            if (dtime.strptime(b['pub_date'], "%Y-%m-%dT%H:%M:%SZ") >= datetime.datetime(year=2016, month=1, day=1)):
                booklist.append(b)
        book_dict = {'match': booklist}
        return JsonResponse({'status': True, 'resp': book_dict})

    return JsonResponse({'status': False, 'resp': 'URL only handles GET requests'})

# make a POST request.
# we urlencode the dictionary of values we're passing up and then make the POST request
# again, no error handling

# print("About to perform the POST request...")
#
# post_data = {'title': 'Demo Post', 'body': 'This is a test', 'userId': 1}
#
# post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
#
# req = urllib.request.Request('http://placeholder.com/v1/api/posts/create', data=post_encoded, method='POST')
# resp_json = urllib.request.urlopen(req).read().decode('utf-8')
#
# resp = json.loads(resp_json)
# print(resp)