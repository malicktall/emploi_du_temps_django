from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name="departement.index"),
    path('add/', add, name="departement.add"),
    path('update/<int:my_id>', update, name="departement.update"),
    path('show/<int:my_id>', show, name="departement.show"),
    path('delate/<int:my_id>', supprimer, name="departement.delate"),

]
