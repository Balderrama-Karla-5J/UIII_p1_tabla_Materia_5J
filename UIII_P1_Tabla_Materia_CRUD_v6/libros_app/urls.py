from django.urls import path
from libros_app import views

urlpatterns = [
    path("", views.inicio_vista, name= "inicio_vista" ),
    path("registrarLibros/",views.registrarLibros,name="registrarLibros"),
       path("seleccionarLibros/<id_libro>",views.seleccionarLibros,name="seleccionarLibros"),
    path("editarLibros/",views.editarLibros,name="editarLibros"),
    path("borrarLibros/<id_libro>",views.borrarLibros,name="borrarLibros"),
    ]