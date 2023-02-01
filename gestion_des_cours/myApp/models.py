from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Max
# Create your models here.


class User(AbstractUser):
    is_enseignant = models.BooleanField(default=False)
    # departements = models.ManyToManyField(null=True, blank=True)




class Matiere(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']


class Departement(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']


class Salle(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']


class Filiere(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']
        
        
# class Promo(models.Model):
#     name = models.CharField(max_length=100)
#     filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE)
    
#     class Meta:
#         ordering = ['name']


class Creneau(models.Model):
   
    date = models.DateField()
    heureDebut = models.TimeField(auto_now=False, auto_now_add=False)
    heureFin = models.TimeField(auto_now=False, auto_now_add=False)
    enseignant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enseignant')
    savedBy = models.ForeignKey(User, on_delete=models.CASCADE, related_name='savedBy')
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE)
    # salle = models.ForeignKey(Salle, on_delete=models.CASCADE)
    types = models.CharField(max_length=20)
    

    class Meta:
        ordering = ['-date']
