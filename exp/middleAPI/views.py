from django.shortcuts import render
import urllib.request
import urllib.parse
import json
from django.http import JsonResponse



def userInfo(request, user_id):
    if(request.method == "GET"):
        req = urllib.request.Request('http://localhost:8001/user_display/' + user_id)
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        resp = json.loads(resp_json)
        return JsonResponse({'status': True, 'resp': resp})

def bookInfo(request, book_id):
    if (request.method == "GET"):
        req = urllib.request.Request('http://localhost:8001/user_display/' + book_id)
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        resp = json.loads(resp_json)
        return JsonResponse({'status': True, 'resp': resp})


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