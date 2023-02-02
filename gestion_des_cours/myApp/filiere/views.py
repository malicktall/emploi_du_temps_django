from django.shortcuts import render, redirect
from myApp.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


@login_required(login_url="/login/")
@staff_member_required

def index(request):
    filiere = Filiere.objects.all()
    return render(request, 'filiere/index.html', {'filiere': filiere})


@login_required(login_url="/login/")
@staff_member_required
def add(request):
    departements = Departement.objects.all()
    if request.method == "POST":
        name = request.POST.get('name')
        departement = request.POST.get('departement')
        
        crenaux_objet = {
            'name': name,
            'departement_id': departement,
        }
        try:
            newFiliere = Filiere.objects.create(**crenaux_objet)
            if newFiliere:
                newFiliere.save()
                messages.success(request, "filiere ajouter avec succès !")
            else:
                messages.error(request, "filiere n'a pas été ajouté  !")
        except Exception as e:
            messages.error(request, f"Vos données ne sont pas correct ! {e}")
            
    return render(request, 'filiere/add.html', {'message': messages, 'departements':departements})


@login_required(login_url="/login/")
@staff_member_required
def update(request, my_id):
    departements = Departement.objects.all()

    filiere = Filiere.objects.get(id=my_id)
    return render(request, 'filiere/update.html', {'filiere': filiere, 'departements': departements} )


def to_update(request, my_id):

    filiere = Filiere.objects.get(id=my_id)
    if request.method == "POST":
        name = request.POST.get('name')
        departement = request.POST.get('departement')
        
        try:
            if filiere:
                filiere.name = name
                filiere.departement_id = departement 
                filiere.save()
                messages.success(request, "filiere modifier avec succès !")
            else:
                messages.error(request, "filiere n'a pas été modifié  !")
                return redirect('filiere.update', my_id, permanent=True)

        except Exception as e:
            messages.error(request, f"Vos données ne sont pas correct ! {e}")
            
            return redirect('filiere.update', my_id, permanent=True)
    context = {
        'message': messages
    }
    return redirect('filiere.index')

@login_required(login_url="/login/")
@staff_member_required
def show(request, my_id):
    filiere = Filiere.objects.get(id=my_id)
    return render(request, 'filiere/show.html', {'filiere': filiere})


@login_required(login_url="/login/")
@staff_member_required
def supprimer(request, my_id):
    filiere = Filiere.objects.get(id=my_id)
    filiere.delete()
    messages.success(request, "filiere supprimer avec succès !")
    return redirect('filiere.index')
