from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def blanco(request):
    return render(request, 'AppHogar/blanco.html')


def cocinas(request):
    return render(request, 'AppHogar/cocinas.html')


def electrodomesticos(request):
    return render(request, 'AppHogar/electrodomesticos.html')
    