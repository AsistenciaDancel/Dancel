import pytest
from vistaprevia.models import Categoria
from vistaprevia.models import Producto 
from vistaprevia.models import Marca
from datetime import date
from django.contrib.auth.models import User

from faker import Faker 
fake=Faker()
#y desp cuando cargamos datofake.filepath()


@pytest.fixture()
def crear_producto_factory(db):
    
    
    def crear_producto(
            nombre: str ="zapato",
            precio: int =2000,
            stock: int = 10,
            fecha_ingreso: date = date.today(),
            categoria_nombre: str = "cat1",
            marca_nombre: str="marca1",
            tipo: str = "Zero",
            tamaños: str = "1K"
            
           
    ):
        marca, _= Marca.objects.get_or_create(nombre=categoria_nombre)
        categoria, _= Categoria.objects.get_or_create(nombre=marca_nombre)

        mi_producto= Producto(
            nombre=nombre,
            precio=precio,
            stock=stock,
            fecha_ingreso=fecha_ingreso,
            categoria=categoria,
            marca=marca,
            tipo=tipo,
            tamaños=tamaños,

        )
        mi_producto.save()
        return mi_producto
    return crear_producto

@pytest.fixture()
def producto(db, crear_producto_factory):
    return crear_producto_factory(fake.name(), 2000, 20, fake.date(), "bebidas", "coca","zero", "1,5")
    
#podemos cargarlo con #fakenake la libreria o directamente con nombrees q le pongamos 