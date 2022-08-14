from django.shortcuts import render, redirect
from django.apps.registry import apps
from .services.source_from_html import LoadHtmlSource
from .models import Node, Link
from django.http import HttpResponse
import json

# Create your views here.
from django.core import serializers


def index(request):
    return HttpResponse("Hello index")



def test(request):

    return HttpResponse("Hello test")



