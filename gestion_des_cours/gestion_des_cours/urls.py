"""gestion_des_cours URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
# from myApp.views import admin_panel
urlpatterns = [
    path('admin/', admin.site.urls),
    
    path("", include("myApp.authentication.urls")),
    path("", include("myApp.home.urls")),
    path("crenaux/", include("myApp.crenaux.urls")),
    path("departement/", include("myApp.departement.urls")),
    path("enseignant/", include("myApp.enseignant.urls")),
    path("matiere/", include("myApp.matiere.urls")),
    path("filiere/", include("myApp.filiere.urls")),
    path("promo/", include("myApp.promo.urls")),
    path("enseignants/", include("myApp.home.enseignant.urls")),
    path("salle/", include("myApp.salle.urls")),
    
    
]
