from django.shortcuts import redirect, render
from django.http import HttpResponse
from AppHogar.models import *
from AppHogar.forms import *

# Create your views here.
def blanco(request):
    return render(request, 'AppHogar/blanco.html')


def cocinas(request):
    return render(request, 'AppHogar/cocinas.html')


def electrodomesticos(request):
    return render(request, 'AppHogar/electrodomesticos.html')

    
# Formulario para cargar blancos
def blancoForm(request):
    if request.method == "POST":

        miFormulario = BlancoFormulario(request.POST)

        if miFormulario.is_valid():
            
            informacion = miFormulario.cleaned_data

            blancoInsta = Blanco(marca=informacion["marca"], descripcion=informacion["descripcion"], color=informacion["color"], plazas=informacion["plazas"],precio=informacion["precio"])

            blancoInsta.save()

            return render(request, 'AppHogar/blanco.html')

    else:

        miFormulario = BlancoFormulario()


    return render (request, 'AppHogar/blancoForm.html ',{'miFormulario':miFormulario})



#Formulario para cargar cocinas 
def cocinaForm(request):
    if request.method == "POST":
        miFormulario = CocinaFormulario(request.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            cocina_insta = Cocinas(marca = informacion["marca"], color=informacion["color"], canti_hornallas=informacion["canti_hornallas"])
            cocina_insta.save()

            return render(request,'AppHogar/cocinas.html')
    else:
            miFormulario = CocinaFormulario()
    return render(request,'AppHogar/cocinaForm.html', {'miFormulario':miFormulario})



#Formulario para cargar electrodomesticos
def electroForm(request):
    if request.method == "POST":
        miFormulario = ElectrodomesticosFormulario(request.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            electro_insta = Electrodomesticos(marca=informacion["marca"], descripcion=informacion["descripcion"],modelo=informacion["modelo"], color=informacion["color"], voltage=informacion["voltage"])
            electro_insta.save()

            return render(request,'AppHogar/electrodomesticos.html')
    else:
            miFormulario = ElectrodomesticosFormulario()
    return render(request,'AppHogar/electroForm.html', {'miFormulario':miFormulario})



