from django.shortcuts import render, redirect
from django.apps.registry import apps
from django.http import HttpResponse
from django.db.models import Q
from .services.visualize import Visualization
from core.models import Node, Link, Attribute

from .forms import SearchForm


# Create your views here.


def index(request):
    return HttpResponse('<h3>hello from visualization plugin</h3>')


def layout(request):
    form = SearchForm()
    a = Visualization()
    plugins = apps.get_app_config('core').source_plugins
    all_nodes = Node.objects.all()
    links = Link.objects.all()
    root = all_nodes[0]
    tree = {}
    tree = a.getTree()
    print(tree)

    # print(tree[root], "-----------------tree root")
    # print(tree, "tree---------------")
    # print(all_nodes)
    print(root, "root")

    return render(request, 'visualization/layout.html', {
        "root": root, "nodes": tree[root], "searchForm": form,
    })


def search(request):

    nodeId = 1609
    form = SearchForm()
    a = Visualization()
    plugins = apps.get_app_config('core').source_plugins
    all_nodes = Node.objects.all()
    links = Link.objects.all()
    root = Node.objects.filter(pk=nodeId)[0]  # todo try except pls
    tree = {}
    tree = a.getSearchTreeById(nodeId)

    print(root, "root")

    return render(request, 'visualization/layout.html', {
        "root": root, "nodes": tree[root],"searchForm": form,
    })


def searchResults(request):
    searchString = ""
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            searchString = form.cleaned_data['search_node']

    if searchString.isdigit():
        results = Node.objects.filter(Q(label=searchString) | Q(text__icontains=searchString) | Q(id=searchString))
    else:
        results = Node.objects.filter(Q(label=searchString) | Q(text__icontains=searchString))

    print(results)

    return render(request, 'visualization/search_results.html', {"results": results})

