from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def index(request):
    return render(request, 'index.html')

def Optical_glass(request):
    return render(request, 'Optical_glass.html')

def Optical_glass_processing_equipment(request):
    return render(request, 'Optical_glass_processing_equipment.html')

def Optical_Instruments(request):
    return render(request, 'Optical_Instruments.html')

def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # İşlem yapmak için form verilerini al
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # E-posta göndermek
            send_mail(
                f"Contact Form Submission from {name}",
                message,
                email,
                [settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )

            # Kullanıcıyı bir başarı sayfasına yönlendirin
            return redirect('contact_success')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

def contact_success(request):
    return render(request, 'contact_success.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
