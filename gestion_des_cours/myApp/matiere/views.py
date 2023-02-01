from django.shortcuts import render, redirect
from myApp.models import *
from django.contrib import messages
from .forms import  MatiereForm, RowMatiereForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


@login_required(login_url="/login/")
@staff_member_required
def index(request):
    matiere = Matiere.objects.all()
    return render(request, 'matiere/index.html', {'matiere': matiere})


@login_required(login_url="/login/")
@staff_member_required
def add(request):
    form = RowMatiereForm()
    if request.method == "POST":
        form = RowMatiereForm(request.POST)
        if form.is_valid():
            newMatiere =  Matiere.objects.create(**form.cleaned_data)
            newMatiere.save()
            messages.success(request, "matiere ajouter avec succès !")
    return render(request, 'matiere/add.html', {'message': messages, 'form':form})


@login_required(login_url="/login/")
@staff_member_required
def update(request, my_id):
    # form = RowMatiereForm()
    matiere = Matiere.objects.get(id=my_id)
    form = MatiereForm(request.POST or None, instance=matiere)
    if form.is_valid():
        form.save()
        form = MatiereForm()
        messages.success(request, "matiere modifier avec succès !")
    return render(request, 'matiere/update.html', {'message': messages, 'form': form})
    

@login_required(login_url="/login/")
@staff_member_required
def show(request, my_id):
    matiere = Matiere.objects.get(id=my_id)
    return render(request, 'matiere/show.html', {'matiere': matiere})


@login_required(login_url="/login/")
@staff_member_required
def supprimer(request, my_id):
    matiere = Matiere.objects.get(id=my_id)
    matiere.delete()
    return redirect('matiere.index')
