from django.http import JsonResponse

# Create your views here.

def api_home(request):
    return JsonResponse ({'message':"hello,django api"})