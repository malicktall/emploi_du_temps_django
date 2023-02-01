from django.urls import path
from .views import *
urlpatterns = [
    path('',index, name="crenaux.index"),
    path('add/', add, name="crenaux.add"),
    path('update/<int:my_id>', update, name="crenaux.update"),
    path('toupdate/<int:my_id>', to_update, name="crenaux.to_update"),
    path('show/<int:my_id>', show, name="crenaux.show"),
    path('delate/<int:my_id>', supprimer, name="crenaux.delate"),
    path('filtrer', filtrer, name="crenaux.filtrer"),
    path('filtrerUnFiliere', filtrerUnFiliere, name="crenaux.filtrerUnFiliere"),
    path('filtrerSemaine', filtrerSemaine, name="crenaux.filtrerSemaine"),
    
]
