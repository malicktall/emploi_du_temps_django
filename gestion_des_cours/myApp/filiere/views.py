from django.shortcuts import render, redirect
from myApp.models import *
from django.contrib import messages
from .forms import FiliereForm, RowFiliereForm
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
    form = RowFiliereForm()
    if request.method == "POST":
        form = RowFiliereForm(request.POST)
        if form.is_valid():
            newfiliere = Filiere.objects.create(**form.cleaned_data)
            newfiliere.save()
            messages.success(request, "Promo ajouter avec succès !")
    return render(request, 'filiere/add.html', {'message': messages, 'form': form})


@login_required(login_url="/login/")
@staff_member_required
def update(request, my_id):
    filiere = Filiere.objects.get(id=my_id)
    form = FiliereForm(request.POST or None, instance=filiere)
    if form.is_valid():
        form.save()
        form = FiliereForm()
        messages.success(request, "Promo modifier avec succès !")
    return render(request, 'filiere/update.html', {'message': messages, 'form': form})


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
    messages.success(request, "Promo supprimer avec succès !")
    return redirect('filiere.index')
