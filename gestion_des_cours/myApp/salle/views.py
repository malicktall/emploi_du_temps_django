from django.shortcuts import render, redirect
from myApp.models import Salle
from django.contrib import messages
from .forms import SalleForm, RowSalleForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


@login_required(login_url="/login/")
@staff_member_required
def index(request):
    salle = Salle.objects.all()
    return render(request, 'salle/index.html', {'salle': salle})


@login_required(login_url="/login/")
@staff_member_required
def add(request):
    form = RowSalleForm()
    if request.method == "POST":
        form = RowSalleForm(request.POST)
        if form.is_valid():
            newsalle = Salle.objects.create(**form.cleaned_data)
            newsalle.save()
            messages.success(request, "salle ajouter avec succès !")
    return render(request, 'salle/add.html', {'message': messages, 'form': form})


@login_required(login_url="/login/")
@staff_member_required
def update(request, my_id):
    salle = Salle.objects.get(id=my_id)
    form = SalleForm(request.POST or None, instance=salle)
    if form.is_valid():
        form.save()
        form = SalleForm()
        messages.success(request, "salle modifier avec succès !")
    return render(request, 'salle/update.html', {'message': messages, 'form': form})


@login_required(login_url="/login/")
@staff_member_required
def show(request, my_id):
    salle = Salle.objects.get(id=my_id)
    return render(request, 'salle/show.html', {'salle': salle})


@login_required(login_url="/login/")
@staff_member_required
def supprimer(request, my_id):
    salle = Salle.objects.get(id=my_id)
    salle.delete()
    return redirect('salle.index')
