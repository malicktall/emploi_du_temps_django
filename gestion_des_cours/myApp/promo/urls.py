from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name="promo.index"),
    path('add/', add, name="promo.add"),
    path('update/<int:my_id>', update, name="promo.update"),
    path('toupdate/<int:my_id>', to_update, name="promo.toupdate"),
    path('show/<int:my_id>', show, name="promo.show"),
    path('delate/<int:my_id>', supprimer, name="promo.delate"),

]
