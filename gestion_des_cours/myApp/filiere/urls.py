from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name="filiere.index"),
    path('add/', add, name="filiere.add"),
    path('update/<int:my_id>', update, name="filiere.update"),
    path('toupdate/<int:my_id>', to_update, name="filiere.toupdate"),
    path('show/<int:my_id>', show, name="filiere.show"),
    path('delate/<int:my_id>', supprimer, name="filiere.delate"),

]
