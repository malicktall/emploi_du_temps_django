from django.shortcuts import render, redirect
from myApp.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


@login_required(login_url="/login/")
@staff_member_required

def index(request):
    promo = Promo.objects.all()
    return render(request, 'promo/index.html', {'promo': promo})


@login_required(login_url="/login/")
@staff_member_required
def add(request):
    filieres = Filiere.objects.all()
    if request.method == "POST":
        name = request.POST.get('name')
        filiere = request.POST.get('filiere')
        
        crenaux_objet = {
            'name': name,
            'filiere_id': filiere,
        }
        try:
            newPromo = Promo.objects.create(**crenaux_objet)
            if newPromo:
                newPromo.save()
                messages.success(request, "promo ajouter avec succès !")
            else:
                messages.error(request, "promo n'a pas été ajouté  !")
        except Exception as e:
            messages.error(request, f"Vos données ne sont pas correct ! {e}")
            
    return render(request, 'promo/add.html', {'message': messages, 'filieres':filieres})


@login_required(login_url="/login/")
@staff_member_required
def update(request, my_id):
    filieres = Filiere.objects.all()

    promo = Promo.objects.get(id=my_id)
    return render(request, 'promo/update.html', {'promo': promo, 'filieres': filieres} )


def to_update(request, my_id):

    promo = Promo.objects.get(id=my_id)
    if request.method == "POST":
        name = request.POST.get('name')
        filiere = request.POST.get('filiere')
        
        try:
            if promo:
                promo.name = name
                promo.filiere_id = filiere 
                promo.save()
                messages.success(request, "promo modifier avec succès !")
            else:
                messages.error(request, "promo n'a pas été modifié  !")
                return redirect('promo.update', my_id, permanent=True)

        except Exception as e:
            messages.error(request, f"Vos données ne sont pas correct ! {e}")
            
            return redirect('promo.update', my_id, permanent=True)
    context = {
        'message': messages
    }
    return redirect('promo.index')

@login_required(login_url="/login/")
@staff_member_required
def show(request, my_id):
    promo = Promo.objects.get(id=my_id)
    return render(request, 'promo/show.html', {'promo': promo})


@login_required(login_url="/login/")
@staff_member_required
def supprimer(request, my_id):
    promo = Promo.objects.get(id=my_id)
    promo.delete()
    messages.success(request, "promo supprimer avec succès !")
    return redirect('promo.index')
