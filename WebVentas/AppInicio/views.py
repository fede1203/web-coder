from django.shortcuts import render
from django.http import HttpResponse


def inicio(request):
    
    return render(request,'AppInicio/inicio.html')


def base(request):
    return render(request, 'AppInicio/base.html')    