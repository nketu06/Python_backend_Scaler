from django.http import HttpResponse,JsonResponse
from demoapp.models import Student
from .serializers import StudentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

def hello_world(request,name):
    # s1=Student(name=name, age=20, dob="2003-01-01", is_active=True)
    # s1.save()
    student = Student.objects.get(name=name)
    print(student,type(student))
    return HttpResponse(f"Hello, {name}! This is a Django application.")



@api_view(['GET', 'POST'])
def hello_student(request, name):
    if request.method == 'POST':
        # Deserialize and validate the incoming JSON data
        data = request.data
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            # Save the validated data to the database
            student = serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            # Return validation errors
            return JsonResponse(serializer.errors, status=400)
    else:
        # Handle GET request
        student = Student.objects.get(name=name)
        serializer = StudentSerializer(student)
        return JsonResponse(serializer.data, status=200)
