from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'index.html')

def Optical_glass(request):
    return render(request, 'Optical_glass.html')

def Optical_glass_processing_equipment(request):
    return render(request, 'Optical_glass_processing_equipment.html')

def Optical_Instruments(request):
    return render(request, 'Optical_Instruments.html')


def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
