from django.http import HttpResponse

# Create your views here.

def hello_world(request,name):
    return HttpResponse(f"Hello, {name}! This is a Django application.")