from django.shortcuts import render, redirect
from django.apps.registry import apps
from django.http import HttpResponse

# Create your views here.


def index(request):

    return HttpResponse('<h3>hello from visualization plugin</h3>')