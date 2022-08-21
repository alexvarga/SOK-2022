from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.apps.registry import apps
from .services.UploadHandlerService import handle_uploaded_file
from .forms import UploadForm


# Create your views here.


def index(request):
    plugins = apps.get_app_config('core').source_plugins
    plugins_vis = apps.get_app_config('core').visualization_plugins
    form = UploadForm()
    return render(request, 'core/index.html', {'source_plugins': plugins, 'form': form, 'vis_plugins': plugins_vis})


def upload(request):
    selected_plugin = 0
    plugins = apps.get_app_config('core').source_plugins
    plugins_vis = apps.get_app_config('core').visualization_plugins

    form = UploadForm()
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        name = request.FILES['file'].name
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])

            plugins[selected_plugin].parse('upload-' + name)  # imam samo jedan source plugin

            return render(request, 'core/vis_list.html', {"vis_plugins": plugins_vis})

            # return HttpResponse(res)
        else:
            form = UploadForm()
    return render(request, 'core/index.html', {'form': form, "vis_plugins": plugins_vis})
