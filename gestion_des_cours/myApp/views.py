from django.shortcuts import render, redirect
from datetime import datetime
from myApp.utils import send_Email_modification
from django.contrib import messages
from myApp.models import *

# Create your views here.

# def admin_panel(request):
#     return render(request, "home/index.html")


def statistique(request):
    
    crenaux_f_info = Creneau.objects.filter(filiere='informatique').count()
    crenaux_f_info = int(crenaux_f_info)
    
    crenaux_f_lpc = Creneau.objects.filter(filiere='lpc').count()
    crenaux_f_lpc = int(crenaux_f_lpc)
    
    crenaux_f_lmio = Creneau.objects.filter(filiere='lmio').count()
    crenaux_f_lmio = int(crenaux_f_lmio)
    
    crenaux_f_lmi = Creneau.objects.filter(filiere='informatique').count()
    crenaux_f_lmi = int(crenaux_f_lmi)
    
    filiere_list = ['informatique', 'lpc', 'lmio', 'lmi']
    crenaux_list = [crenaux_f_info, crenaux_f_lmio, crenaux_f_lmi, crenaux_f_lpc]
    
    context = {
        'filiere_list':filiere_list,
        'crenaux_list':crenaux_list
    }
    
    return render(request, 'home/index.html', context)
    # crenaux_f_info = Creneau.objects.filter(filiere='informatique').count()
    # crenaux_f_info = int(crenaux_f_info)
    
    # crenaux_f_info = Creneau.objects.filter(filiere='informatique').count()
    # crenaux_f_info = int(crenaux_f_info)