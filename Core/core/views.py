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


def test(request):
    plugins = apps.get_app_config('core').source_plugins
    return render(request, 'core/test.html', {})


def upload(request):
    plugins = apps.get_app_config('core').source_plugins
    plugins_vis = apps.get_app_config('core').visualization_plugins

    form = UploadForm()
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        name = request.FILES['file'].name
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            for item in plugins:  # TODO ovo ovde ne treba da bude, već treba za svaki source plagin da postoji poseban uploader
                item.parse('upload-' + name) #for petlja nepotrebna jer svaki source plugin treba ima svoj Parse

            res = "Visualisation visualization </br>"
            for item in plugins_vis:
                res += "<a href=/" + item.location + "/layout>" + item.name + "</a>"

            return HttpResponse(res)
        else:
            form = UploadForm()
    return render(request, 'core/index.html', {'form': form})
