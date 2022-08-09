from django.shortcuts import render, redirect
from django.apps.registry import apps
from .services.source_from_html import LoadHtmlSource

# Create your views here.


def index(request):

    a = LoadHtmlSource()
    a.parseHTML()
    return redirect('../../core')