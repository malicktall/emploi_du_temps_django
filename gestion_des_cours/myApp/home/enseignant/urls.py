# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from myApp.home.enseignant import views

urlpatterns = [

    # The home page
    path('mescours', views.mescours, name='mescours'),
    path('show/<int:my_id>', views.show, name='show'),
    path('update/<int:my_id>', views.update, name='update'),

]
