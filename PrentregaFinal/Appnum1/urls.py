from django.urls import path
from Appnum1.views import *
from Appnum1.models import *

urlpatterns = [
    path("", inicio, name= "inicio"),
    path("colab/", trabajadores, name="Trabajadores"),
    path("comprador/", comprador, name = "compradores"),
    path("vendedores/", vendedores, name = "vendedores"),
    path("formulario1/", colabformulario, name="fcolab"),
    path("formulario2/", buyerformulario, name="fbuyer"),
    path("formulario3/", sellerformulario, name="fseller"),
    path("resultados/", resultados, name="resulegajo"),
]