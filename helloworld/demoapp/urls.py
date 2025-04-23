from django.urls import path
from demoapp import views

urlpatterns=[path('hello/<name>',views.hello_world,name='hello_world')]