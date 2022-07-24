from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.
def say_hello_in_html(request):
    # return HttpResponse("Hello World")
    return render(request,'hello.html',{"name":"Prabin"})
 
@api_view(["GET"]) 
def say_hello_in_json(request):
    return Response({
        "message":"Hello in json format"
    })