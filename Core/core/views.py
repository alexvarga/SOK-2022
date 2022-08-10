from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.apps.registry import apps
from .services.UploadHandlerService import handle_uploaded_file
from .forms import UploadForm


# Create your views here.


def index(request):
    plugins = apps.get_app_config('core').source_plugins
    form = UploadForm()
    return render(request, 'core/index.html', {'source_plugins': plugins, 'form': form})


def upload(request):
    plugins = apps.get_app_config('core').source_plugins

    form = UploadForm()
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse("FILE UPLOADED SUCCESSFULLY")
        else:
            form = UploadForm()
    return render(request, 'blog/home.html', {'form': form})
