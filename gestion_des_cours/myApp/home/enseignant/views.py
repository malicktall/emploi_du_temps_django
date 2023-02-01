from django.shortcuts import render, redirect
from myApp.models import *
from django.contrib import messages
from .forms import CreneauForm, RowCreneauForm
from django.contrib.auth.decorators import login_required
from datetime import datetime
from myApp.utils import send_Email_modification


@login_required(login_url="/login/")
def mescours(request):
    my_id = request.user.id
    print(f" my id est : {my_id}")
    my_id = int(my_id)
    cours = Creneau.objects.filter(enseignant=my_id)
    return render(request, 'home/enseignant/mescours.html', {'cours': cours})



@login_required(login_url="/login/")
def update(request, my_id):
    enseignants = User.objects.all()
    matieres = Matiere.objects.all()
    filieres = Filiere.objects.all()
    crenaux = Creneau.objects.get(id=my_id)
    
    enseignant = request.user
    print(f"l'email est : {enseignant.email}")
        
    if request.method == 'POST':
        date = request.POST.get('date')
        heureDebut = request.POST.get('heureDebut')
        heureFin = request.POST.get('heureFin')
        enseignant = request.user
        savedBy = crenaux.savedBy.email
        id_mat = request.POST.get('matiere')
        types = request.POST.get('types')

        if heureDebut >= heureFin:
            messages.error(
                request, "l'heure debut ne doit pas inferieur ou egal a heure fin")
            return redirect('update', my_id, permanent=True)
        
        template = 'email.html'
        subject = "Demande de modification"
        context = {
            'id':my_id,
            'date': date,
            'heureDebut':heureDebut,
            'heureFin':heureDebut,
            'types':types,
            'name': enseignant,

        }

        receivers = [enseignant.email, savedBy]

        has_send = send_Email_modification(
            subject=subject, receivers=receivers, template=template, context=context)

        if has_send:
            messages.success(request, " Demande de modification envoyé avec succès")
        else:
            messages.error(request, "echec envoi de demande")

    return render(request, 'home/enseignant/update.html', {'crenaux': crenaux,
      'enseignants': enseignants, 'matieres': matieres, 'filieres': filieres, 'message': messages})



@login_required(login_url="/login/")
def show(request, my_id):
    crenaux = Creneau.objects.get(id=my_id)
    return render(request, 'home/enseignant/show.html', {'crenaux': crenaux})


@login_required(login_url="/login/")
def supprimer(request, my_id):
    matiere = Matiere.objects.get(id=my_id)
    matiere.delete()
    return redirect('matiere.index')
