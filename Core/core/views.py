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

    form = UploadForm()
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        name = request.FILES['file'].name
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            for item in plugins:
                item.parse('upload-'+name)
            return HttpResponse("go to visualization")
        else:
            form = UploadForm()
    return render(request, 'core/index.html', {'form': form})
