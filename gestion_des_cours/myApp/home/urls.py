# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from myApp.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='index'),
    path('home', views.home, name="home"),
    path('enseignant/home', views.enseignant, name="enseignant.home")
    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),

]
