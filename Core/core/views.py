from django.shortcuts import render
from django.apps.registry import apps


# Create your views here.


def index(request):
    plugins = apps.get_app_config('core').source_plugins
    return render(request, 'core/index.html', {'source_plugins': plugins})