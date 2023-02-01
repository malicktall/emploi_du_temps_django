from django.shortcuts import render, redirect
from myApp.models import *
from django.contrib import messages
from .forms import CreneauForm, RowCreneauForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import JsonResponse


@login_required(login_url="/login/")
@staff_member_required
def index(request):
    crenaux = Creneau.objects.all()
    
    days = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche']
    # context = {
    #     'crenaux': crenaux
    # }
    return render(request, 'crenaux/index.html', {'crenaux': crenaux, 'days':days})


@login_required(login_url="/login/")
@staff_member_required
def events(request):
    
    events = Creneau.objects.all().values('date', 'heureDebut', 'heureFin', 'matiere')
    return JsonResponse(list(events), safe=False)
    # return render(request, 'crenaux/index.html', {'crenaux': crenaux, 'days':days})


@login_required(login_url="/login/")
@staff_member_required
def add(request, *args, **kwargs):
    enseignants = User.objects.all()
    matieres = Matiere.objects.all()
    filieres = Filiere.objects.all()

    if request.method == "POST":
        date = request.POST.get('date')
        date1 = request.POST.get('date')
        heureDebut = request.POST.get('heureDebut')
        heureFin = request.POST.get('heureFin')
        enseignant = request.POST.get('enseignant')
        matiere = request.POST.get('matiere')
        filiere = request.POST.get('filiere')
        types = request.POST.get('types')
        savedBy = request.user
        if heureDebut >= heureFin:
            messages.error(
                request, "l'heure debut ne doit pas inferieur ou egal a heure fin")
            return redirect('crenaux.add')

        crenaux = Creneau.objects.all()
        heureDebut = str(heureDebut + ":00")

        for crenau in crenaux:
            # print(crenau.date )
            # print("les date sont egaux")
            date_crenaux = str(crenau.date)
            heure_crenaux = str(crenau.heureDebut)
            id_crenaux = str(crenau.filiere.id)
            # print(date_crenaux)
            print(f"{crenau.filiere.id} --- {filiere}")
            # print(filiere)
            if date_crenaux == date and heure_crenaux == heureDebut and id_crenaux == filiere:
                print("les date sont egaux")
                messages.error(
                    request, "On ne peut pas avoir deux crenaux a la meme date et heure sur le meme promo")
                return redirect('crenaux.add')

        crenaux_objet = {
            'date': date,
            'heureDebut': heureDebut,
            'heureFin': heureFin,
            'enseignant_id': enseignant,
            'matiere_id': matiere,
            'filiere_id': filiere,
            'types': types,
            'savedBy':savedBy
        }

        try:
            newCrenaux = Creneau.objects.create(**crenaux_objet)
            if newCrenaux:
                newCrenaux.save()
                messages.success(request, "Crenaux ajouter avec succès !")
            else:
                messages.error(request, "Crenaux n'a pas été ajouté  !")
        except Exception as e:
            messages.error(request, f"Vos données ne sont pas correct ! {e}")
    context = {
        'enseignants': enseignants,
        'matieres': matieres,
        'filieres': filieres,
        'message': messages
    }
    return render(request, 'crenaux/add.html', context)


# def add(request):
#     form = RowCreneauForm()
#     if request.method == "POST":
#         form = RowCreneauForm(request.POST)
#         if form.is_valid():
#             newCrenaux = Creneau.objects.create(**form.cleaned_data)
#             newCrenaux.save()
#             messages.success(request, "Crenaux ajouter avec succès !")
#     return render(request, 'crenaux/add.html', {'message': messages, 'form': form})


# def update(request, my_id):
#     # form = RowMatiereForm()
#     crenaux = Creneau.objects.get(id=my_id)
#     form = CreneauForm(request.POST or None, instance=crenaux)
#     if form.is_valid():
#         form.save()
#         form = CreneauForm()
#         messages.success(request, "Crenaux modifier avec succès !")
#     return render(request, 'crenaux/update.html', {'message': messages, 'form': form})

@login_required(login_url="/login/")
@staff_member_required
def update(request, my_id):
    enseignants = User.objects.all()
    matieres = Matiere.objects.all()
    filieres = Filiere.objects.all()

    crenaux = Creneau.objects.get(id=my_id)
    return render(request, 'crenaux/update.html',
                  {'crenaux': crenaux, 'enseignants': enseignants,
                   'matieres': matieres, 'filieres': filieres}
                  )


def to_update(request, my_id):

    crenaux = Creneau.objects.get(id=my_id)
    if request.method == "POST":
        date = request.POST.get('date')
        heureDebut = request.POST.get('heureDebut')
        heureFin = request.POST.get('heureFin')
        enseignant = request.POST.get('enseignant')
        matiere = request.POST.get('matiere')
        filiere = request.POST.get('filiere')
        types = request.POST.get('types')
        savedBy = request.user

        if heureDebut >= heureFin:
            messages.error(
                request, "l'heure debut ne doit pas inferieur ou egal a heure fin")
            return redirect('crenaux.update', my_id, permanent=True)
        try:
            if crenaux:
                crenaux.date = date
                crenaux.heureDebut = heureDebut
                crenaux.heureFin = heureFin
                crenaux.enseignant_id = enseignant
                crenaux.matiere_id = matiere
                crenaux.filiere_id = filiere
                crenaux.types = types
                crenaux.savedBy_id = savedBy
                crenaux.save()
                messages.success(request, "Crenaux modifier avec succès !")
            else:
                messages.error(request, "Crenaux n'a pas été modifié  !")
                return redirect('crenaux.update', my_id, permanent=True)

        except Exception as e:
            messages.error(request, f"Vos données ne sont pas correct ! {e}")
            # return redirect('crenaux.to_update')
            # return render(request, 'crenaux/update.html', {'crenaux': crenaux})
            return redirect('crenaux.update', my_id, permanent=True)
    context = {
        'message': messages
    }
    return redirect('crenaux.index')


@login_required(login_url="/login/")
@staff_member_required
def show(request, my_id):
    crenaux = Creneau.objects.get(id=my_id)
    return render(request, 'crenaux/show.html', {'crenaux': crenaux})


@login_required(login_url="/login/")
@staff_member_required
def supprimer(request, my_id):
    crenaux = Creneau.objects.get(id=my_id)
    crenaux.delete()
    return redirect('crenaux.index')


@login_required(login_url="/login/")
@staff_member_required
def filtrerUnFiliere(request):
    try:
        filiere = request.POST.get('filiere')
        fil = Filiere.objects.get(name=filiere)
        id = fil.id
        crenaux = Creneau.objects.filter(filiere=id)
        return render(request, 'crenaux/index.html', {'crenaux': crenaux})
    except Filiere.DoesNotExist:
        messages.error(request, "Ce filiere n'existe pas !")
        return redirect('crenaux.index')


@login_required(login_url="/login/")
@staff_member_required
def filtrerSemaine(request):
    week = request.POST.get('debutSemaine')
    crenaux = Creneau.objects.filter(date__week=week)
    return render(request, 'crenaux/index.html', {'crenaux': crenaux})


@login_required(login_url="/login/")
@staff_member_required
def filtrer(request):
    return render(request, 'crenaux/filtrer.html')
