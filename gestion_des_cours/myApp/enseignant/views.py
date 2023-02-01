from django.shortcuts import render, redirect
from myApp.models import User
from django.contrib import messages
from .forms import EnseignantForm, RowEnseignantForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


@login_required(login_url="/login/")
@staff_member_required
def index(request):
    enseignant = User.objects.filter(is_enseignant='True')
    return render(request, 'enseignant/index.html', {'enseignant': enseignant})


@login_required(login_url="/login/")
@staff_member_required
def add(request):
    form = EnseignantForm()
    if request.method == "POST":
        form = EnseignantForm(request.POST or None)
        if form.is_valid():

            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            form = RowEnseignantForm()
            messages.success(request, "enseignant ajouter avec succès !")
    return render(request, 'enseignant/add.html', {'message': messages, 'form': form})


@login_required(login_url="/login/")
@staff_member_required
def update(request, my_id):
    enseignant = User.objects.get(id=my_id)
    form = EnseignantForm(request.POST or None, instance=enseignant)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        form.save()
        form = EnseignantForm()
        messages.success(request, "enseignant modifier avec succès !")
    return render(request, 'enseignant/update.html', {'message': messages, 'form': form})


@login_required(login_url="/login/")
@staff_member_required
def show(request, my_id):
    enseignant = User.objects.get(id=my_id)
    return render(request, 'enseignant/show.html', {'enseignant': enseignant})


@login_required(login_url="/login/")
@staff_member_required
def supprimer(request, my_id):
    enseignant = User.objects.get(id=my_id)
    enseignant.delete()
    return redirect('enseignant.index')
