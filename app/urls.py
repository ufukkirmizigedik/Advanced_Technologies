from django.urls import path
from .views import index, Optical_glass, Optical_glass_processing_equipment, Optical_Instruments, about, contact, contact_form, contact_success

urlpatterns = [
    path('', index, name='index'),
    path('Optical_glass/', Optical_glass, name='Optical_glass'),
    path('Optical_glass_processing_equipment/', Optical_glass_processing_equipment, name='Optical_glass_processing_equipment'),
    path('Optical_Instruments/', Optical_Instruments, name='Optical_Instruments'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('contact_form/', contact_form, name='contact_form'),  # Corrected URL for contact_form
    path('contact-success/', contact_success, name='contact_success'),  # Use contact_success view
]
