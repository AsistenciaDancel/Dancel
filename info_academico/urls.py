
 
from django.urls import path
from . import views #estoy diciendo que desde vista previa importo views que es mi controlador secundario

urlpatterns = [
    #en este path no ponemos nada porque estamos llamando a una funcion en todo caso en la urls.py principal gramiSys aclaramos las dos vista
    path('', views.index, name='home'), #funcion index en views 


]


    
