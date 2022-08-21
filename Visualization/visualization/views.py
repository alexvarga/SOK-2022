from django.shortcuts import render, redirect
from django.apps.registry import apps
from django.http import HttpResponse, Http404
from django.db.models import Q
from .services.visualize import Visualization
from core.models import Node, Link, Attribute

from .forms import SearchForm


# Create your views here.


def index(request):
    return HttpResponse('<h3>hello from visualization plugin</h3>')


def layout(request):
    plugins_vis = apps.get_app_config('core').visualization_plugins

    form = SearchForm()
    a = Visualization()
    plugins = apps.get_app_config('core').source_plugins
    all_nodes = Node.objects.all()
    links = Link.objects.all()
    root = all_nodes[0]
    tree = {}
    tree = a.getTree()


    return render(request, 'visualization/layout.html', {
        "root": root, "nodes": tree[root], "searchForm": form, "vis_plugins": plugins_vis,
    })


def searchSubTree(request):
    plugins_vis = apps.get_app_config('core').visualization_plugins

    try:
        node = request.GET['node']
    except:
        raise Http404

    nodeId = node
    form = SearchForm()
    a = Visualization()
    plugins = apps.get_app_config('core').source_plugins
    all_nodes = Node.objects.all()
    links = Link.objects.all()
    try:
        root = Node.objects.filter(pk=nodeId)[0]
    except:
        raise Http404
    tree = {}
    tree = a.getSearchTreeById(nodeId)

    return render(request, 'visualization/layout.html', {
        "root": root, "nodes": tree[root], "searchForm": form, "vis_plugins": plugins_vis,
    })


def searchResults(request):
    plugins_vis = apps.get_app_config('core').visualization_plugins

    searchString = ""
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            searchString = form.cleaned_data['search_node']

    if searchString.isdigit():
        results = Node.objects.filter(Q(label=searchString) | Q(text__icontains=searchString) | Q(id=searchString))
    else:
        results = Node.objects.filter(Q(label=searchString) | Q(text__icontains=searchString))

    return render(request, 'visualization/search_results.html', {"results": results, "vis_plugins": plugins_vis, })
