from multiprocessing import context
from django.http import HttpResponse
import datetime
from django.template import Context, Template

def saludar(request):
    return HttpResponse("Hola mundo!")

def segunda_vista(request):
    return HttpResponse("Esta es la segunda vista, ashe")

def diaDeHoy(request):
    
        dia= datetime.datetime.now()

        documentoDeTexto =f"Hoy es dia: <br> {dia}"

        return HttpResponse(documentoDeTexto)

def saludo_con_nombre(self, nombre):

    return HttpResponse("<h1>Hola mi nombre es: "+nombre+"</h1>")

def year_de_nacimiento(self, edad):
    
    return HttpResponse("<h1>Tu año de nacimiento es: "+str(int(datetime.datetime.now().year)-int(edad))+"</h1>")

def probandoHtml(self):
    miArchivo=open("/Users/ianmunna/Documents/CoderHouse/Proyecto1/Proyecto1/Plantillas/template1.html")

    plantilla=Template(miArchivo.read())#leemos el archivo y lo guardamos en una variable
    miArchivo.close()
    
    contexto=Context()#creamos un contexto vacio

    documento=plantilla.render(contexto)

    return HttpResponse(documento)

