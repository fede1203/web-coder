from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    
    return render(request,'AppInicio/inicio.html')


def base(request):
    return render(request, 'AppInicio/base.html')    