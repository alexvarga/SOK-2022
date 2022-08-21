from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('layout', views.layout, name='layout'),
    path('subtree', views.searchSubTree, name='search'),
    path('searchResults', views.searchResults, name='searchResults'),

]


