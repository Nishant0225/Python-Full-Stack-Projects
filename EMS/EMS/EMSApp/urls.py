from django.urls import path
from . import views

urlpatterns=[
    path("",views.index),
    path("dashboard",views.dashboard,name="dashboard"),
    path("addemp",views.addemp,name="addemp"),
    path("listemp",views.listemp,name="listemp"),
    path("searchemp",views.searchemp,name="searchemp"),
    path("deleteemp/<id>",views.deleteemp,name="deleteemp"),

]