from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name="enseignant.index"),
    path('add/', add, name="enseignant.add"),
    path('update/<int:my_id>', update, name="enseignant.update"),
    # path('toupdate/<int:my_id>', to_update, name="enseignant.to_update"),
    path('show/<int:my_id>', show, name="enseignant.show"),
    path('delate/<int:my_id>', supprimer, name="enseignant.delate"),

]
