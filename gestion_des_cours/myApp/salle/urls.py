from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name="salle.index"),
    path('add/', add, name="salle.add"),
    path('update/<int:my_id>', update, name="salle.update"),
    path('show/<int:my_id>', show, name="salle.show"),
    path('delate/<int:my_id>', supprimer, name="salle.delate"),

]
