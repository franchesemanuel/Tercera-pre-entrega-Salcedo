from django.urls import path
from . import views


urlpatterns = [
    path("", views.inicio , name="home"),#agrego los name para llamarlas luego en los link 
    path("ver_cursos", views.ver_cursos , name="cursos"),
    
    path("alumnos" , views.alumnos ,name="alumnos"),
    #path("alta_curso/<nombre>", views.alta_curso),
    path("profesores", views.profesores , name="profesores"),
    path("alta_curso", views.curso_formulario ,name="formulario_curso"),
    path ("buscar_curso", views.buscar_curso ,name="buscar_curso"),
    path("buscar", views.buscar)
]

