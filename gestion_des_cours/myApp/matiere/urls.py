from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name="matiere.index"),
    path('add/', add, name="matiere.add"),
    path('update/<int:my_id>', update, name="matiere.update"),
    # path('toupdate/<int:my_id>', to_update, name="matiere.to_update"),
    path('show/<int:my_id>', show, name="matiere.show"),
    path('delate/<int:my_id>', supprimer, name="matiere.delate"),

]
