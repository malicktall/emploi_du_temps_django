# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render
from myApp.models import *

# @login_required(login_url="/login/")
# def index(request):
#     context = {'segment': 'index'}

#     html_template = loader.get_template('home/index.html')
#     return HttpResponse(html_template.render(context, request))


# @login_required(login_url="/login/")
# def pages(request):
#     context = {}
#     # All resource paths end in .html.
#     # Pick out the html file name from the url. And load that template.
#     try:

#         load_template = request.path.split('/')[-1]

#         if load_template == 'admin':
#             return HttpResponseRedirect(reverse('admin:index'))
#         context['segment'] = load_template

#         html_template = loader.get_template('home/' + load_template)
#         return HttpResponse(html_template.render(context, request))

#     except template.TemplateDoesNotExist:

#         html_template = loader.get_template('home/page-404.html')
#         return HttpResponse(html_template.render(context, request))

#     except:
#         html_template = loader.get_template('home/page-500.html')
#         return HttpResponse(html_template.render(context, request))
@login_required(login_url="/login/")
def home(request):
    return render(request, 'home/home.html')


@login_required(login_url="/login/")
def index(request):
    
    crenaux_f_info = Creneau.objects.filter(filiere_id=1).count()
    crenaux_f_info = int(crenaux_f_info)

    crenaux_f_lpc = Creneau.objects.filter(filiere_id=2).count()
    crenaux_f_lpc = int(crenaux_f_lpc)

    crenaux_f_lmio = Creneau.objects.filter(filiere_id=4).count()
    crenaux_f_lmio = int(crenaux_f_lmio)

    crenaux_f_lmi = Creneau.objects.filter(filiere_id=5).count()
    crenaux_f_lmi = int(crenaux_f_lmi)

    filiere_list = ['lgi', 'lmio', 'lmi', 'lpc']
    crenaux_list = [crenaux_f_info, crenaux_f_lmio,
                    crenaux_f_lmi, crenaux_f_lpc]

    matieres = Matiere.objects.all().count()
    matieres = int(matieres)
    
    departement = Departement.objects.all().count()
    departement = int(departement)
    
    filieres = Filiere.objects.all().count()
    filieres = int(filieres)
    
    salles = Salle.objects.all().count()
    salles = int(salles)
    
    lists = ['matieres', 'departement', 'filieres', 'salles']
    objets = [matieres, departement,
              filieres, salles]

    enseignant = User.objects.filter(is_enseignant='True').count()
    enseignant = int(enseignant)
    
    user = User.objects.filter(is_enseignant='False').count()
    user = int(user)
    
    personnes = ['enseignant', 'administrateur']
    nombres = [enseignant, user]
    
    context = {
        'filiere_list': filiere_list,
        'crenaux_list': crenaux_list,
        'lists':lists,
        'objets':objets,
        'personnes': personnes,
        'nombres': nombres
    }

    return render(request, 'home/index.html', context)


@login_required(login_url="/login/")
def enseignant(request):
    return render(request, 'home/enseignant/index.html')


