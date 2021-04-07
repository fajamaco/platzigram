from django.urls import path
from django.http import HttpResponse


def hello_world(request):
    return HttpResponse('Hello')


urlpatterns = [

    path('hello-world/', hello_world)
  
]
