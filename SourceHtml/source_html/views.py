from django.shortcuts import render, redirect
from django.apps.registry import apps
from .services.source_from_html import LoadHtmlSource
from .models import Node
from django.http import HttpResponse
import json

# Create your views here.
from django.core import serializers



def index(request):

    a = LoadHtmlSource()
    a.parse()

def test(request):
    a=LoadHtmlSource()
    nodes = Node.objects.all()
    c= a.getTree()
    # mtj = a.my_to_json(nodes)
    aaa = a.my_to_json(nodes)
    print(aaa)



    return HttpResponse("Hello, ")

