from django.template import loader 
from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.forms import Curso_formulario
from AppCoder.models import Curso
 
#from AppCoder.forms import Curso_formulario

# Create your views here.

def inicio(request):
    return render( request , "padre.html")

 

def alta_curso(request,nombre):
     curso = Curso(nombre=nombre , camada=2341)
     curso.save()
     texto = f"se guardo en la base de datos :{curso.nombre} {curso.camada}"
     return HttpResponse(texto)
 
def ver_cursos(request):
    cursos= Curso.objects.all()# saco todo los objetos del tipo curso de la base de datos ,traeme del modelo cursos todo los objetos 
    dicc = {"cursos": cursos} # la lista de cursos lo guardo en un diccionario 
    plantilla = loader.get_template("cursos.html")# cargo el template
    documento = plantilla.render(dicc)  #del metodo plantilla 
    return HttpResponse(documento)

def alumnos(request):
    return render(request , "alumnos.html")
def profesores(request):
    return render(request , "profesores.html")


def curso_formulario(request):
    if request.method =="POST":
        
        mi_formulario = Curso_formulario( request.POST )
        
        if mi_formulario.is_valid():
            
            datos = mi_formulario.cleaned_data
            curso = Curso ( nombre=datos["nombre"] ,  camada=datos["camada"])
            curso.save()
            return render (request, "formulario.html")
    
    
    return render(request , "formulario.html")



def buscar_curso(request):
    return render(request, "buscar_curso.html")

def buscar(request):
    nombre = request.GET.get("nombre")
    if nombre:
        cursos = Curso.objects.filter(nombre__icontains=nombre)
        return render(request, "resultado_busqueda.html", {"cursos": cursos})
    else:
        return HttpResponse("Por favor, ingrese el nombre del curso.")