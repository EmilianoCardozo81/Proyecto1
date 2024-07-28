from datetime import datetime as dt
from django.http import HttpResponse
# Agregamos al encabezado del archivo el import de Template y de Context
from django.template import Template, Context
from django.template import loader

def saludo(request):
    return HttpResponse("Hola mundo!, hola a Todos! buenas noches")

def pepito(request):
    texto = "soy pepito arturo <br> cursando python"
    return HttpResponse(texto)

def dia_de_hoy(request,dia2):
    dia = dt.now()  
    dia = dia.strftime("%Y-%m-%d")
    dia = dia [:-2]+dia2
    texto = f"Hoy es; <br>{dia}"
    return HttpResponse(texto)




def probando_template(request):
    nombre = "Pepe"
    apellido = "Arturo"
    diccionario = {
        "nombre": nombre,
        "apellido": apellido,
        "notas": [4, 8, 9, 10, 7, 8]
    }
    plantilla = loader.get_template('index.html')
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)

