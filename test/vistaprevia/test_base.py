import pytest
from vistaprevia.models import Producto 
from vistaprevia.models import Marca
from django.contrib.auth.models import User


"""
@pytest.mark.django_db
def test_cambiar_estado(crear_productoAgua):
    print("Cambio de precio producto")
    assert crear_productoAgua.precio ==800
"""

@pytest.mark.django_db
def test_crear_producto():
    marca=Marca.objects.create(nombre="CBC")
    mi_producto=Producto(nombre= "Yerba", marca=marca, stock=20, precio=2000)
    mi_producto.save()
    print(mi_producto.nombre)
    assert mi_producto.nombre =="Yerba"


#testeo que tipo producto sea igual al producto que cree en confitest
@pytest.mark.django_db
def test_cambiar_tipo(producto):
    print(producto.tipo)
    print(producto.nombre)
    print(producto.fecha_ingreso)
    assert producto.tipo=="zero"
