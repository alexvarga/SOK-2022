from django.shortcuts import render, redirect
from django.apps.registry import apps


# Create your views here.


def index(request):

    return redirect('../../core')