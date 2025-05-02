from django.http import HttpResponse
from demoapp.models import Student

# Create your views here.

def hello_world(request,name):
    # s1=Student(name=name, age=20, dob="2003-01-01", is_active=True)
    # s1.save()
    student = Student.objects.get(name=name)
    print(student,type(student))
    return HttpResponse(f"Hello, {name}! This is a Django application.")