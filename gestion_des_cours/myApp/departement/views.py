from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from myApp.models import Departement
from django.contrib import messages
from .forms import DepartementForm, RowDepartementForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required



@login_required(login_url="/login/")
@staff_member_required
def index(request):
    departement = Departement.objects.all()
    return render(request, 'departement/index.html', {'departement': departement})


@login_required(login_url="/login/")
@staff_member_required
def add(request):
    form = RowDepartementForm()
    if request.method == "POST":
        form = RowDepartementForm(request.POST)
        if form.is_valid():
            newdepartement = Departement.objects.create(**form.cleaned_data)
            newdepartement.save()
            messages.success(request, "departement ajouter avec succès !")
    return render(request, 'departement/add.html', {'message': messages, 'form': form})


@login_required(login_url="/login/")
@staff_member_required
def update(request, my_id):
    departement = Departement.objects.get(id=my_id)
    form = DepartementForm(request.POST or None, instance=departement)
    if form.is_valid():
        form.save()
        form = DepartementForm()
        messages.success(request, "departement modifier avec succès !")
    return render(request, 'departement/update.html', {'message': messages, 'form': form})


@login_required(login_url="/login/")
@staff_member_required
def show(request, my_id):
    departement = Departement.objects.get(id=my_id)
    return render(request, 'departement/show.html', {'departement': departement})


@login_required(login_url="/login/")
@staff_member_required
def supprimer(request, my_id):
    departement = Departement.objects.get(id=my_id)
    departement.delete()
    return redirect('departement.index')
