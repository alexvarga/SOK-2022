from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('layout', views.layout, name='layout'),
    path('search', views.search, name='search'),
    path('simple', views.simple, name='simple'),
    path('searchResults', views.searchResults, name='searchResults'),

]


