import json

from django.http import JsonResponse

# Create your views here.

def api_home(request,*args,**kwargs):

    body=request.body
    data={}
    try:
        data=json.loads(body)
        data['params'] = dict(request.GET)
        data['headers'] = dict(request.headers)
        data['content_type'] = dict(request.content_type)
    except:
        pass
    print(data)


    return JsonResponse ({'message':"hello,django api"})