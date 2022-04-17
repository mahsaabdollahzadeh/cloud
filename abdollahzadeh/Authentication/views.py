from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def Authentication(request):
    return HttpResponse("Authentication app ....")

