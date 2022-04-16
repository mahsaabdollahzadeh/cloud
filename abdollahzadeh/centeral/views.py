from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def centeral(request):
    return HttpResponse("centeral app ....")

