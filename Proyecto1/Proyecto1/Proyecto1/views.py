from django.http import HttpResponse


def saludar(reques):
    return HttpResponse("Hola mundo!")

    