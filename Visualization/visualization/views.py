from django.shortcuts import render, redirect
from django.apps.registry import apps
from django.http import HttpResponse
from .services.visualize import Visualization
from source_html.models import Node, Link, Attribute


# Create your views here.


def index(request):

    return HttpResponse('<h3>hello from visualization plugin</h3>')

def layout(request):
    a = Visualization()
    plugins = apps.get_app_config('core').source_plugins
    all_nodes = Node.objects.all()
    links = Link.objects.all()
    root = all_nodes[0]
    tree = {}
    tree = a.getTree()

    # print(tree[root], "-----------------tree root")
    # print(tree, "tree---------------")
    # print(all_nodes)
    print(root, "root")

    return render(request, 'core/layout.html', {
         "root": root, "nodes": tree[root],
    })