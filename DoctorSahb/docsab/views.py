from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.urls import reverse
from .models import *
from .forms import *
from django.core.mail import send_mail,EmailMessage
from django.contrib.auth.views import LoginView
from .models import *
from django.conf import settings

# Create your views here.

class CustomLoginView(LoginView):
    template_name='docsab/login.html'
    fields='__all__'
    redirect_authenticated_user = False

    def get_success_url(self):
        success_url = self.request.GET.get('next')
        if success_url:
            return success_url
        return reverse('index')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)

    #     # Retrieve the doctor and slot objects from your database or any other method
    #     doctor = Doctor.objects.get(pk=1)  # Replace 'pk=1' with your actual lookup condition
    #     slot = Slot.objects.get(pk=2)  # Replace 'pk=2' with your actual lookup condition

    #     # Add the doctor and slot objects to the context
    #     context['doctor'] = doctor
    #     context['slot'] = slot

    #     return context

def index(request):
    return render(request,"docsab/index.html",{
        "data":"Test data"
    })

def all_doctors(request):
    doctors_list= Doctor.objects.all()
    return render(request,"docsab/all_doctors.html",{
        "doctors":doctors_list
    })

def doctor(request,slug):
    
    doctor_details=Doctor.objects.get(pk=slug)
    doctor_hospital_list=doctor_details.hospital_set.all()
    return render(request,"docsab/doctor.html",{
        "doctor":doctor_details,
        "hosps":doctor_hospital_list,
    })

def doctor_slots(request,slug):
    doctor_details=Doctor.objects.get(pk=slug)
    doctor_slots=doctor_details.time_slots.all()
    doctor_hospital_list=doctor_details.hospital_set.all()
    unbooked_slots = doctor_slots.exclude(booking__isnull=False)
    return render(request,"docsab/doctor_slots.html",{
        "doctor":doctor_details,
        "hosps":doctor_hospital_list,
        "slots":unbooked_slots,
    })

def doctor_booking(request,slug1,slug2):
    
    
        patient_name= request.user.patient

        slot= TimeSlot.objects.get(pk=slug2)
        doctor_details=Doctor.objects.get(pk=slug1)
        return render(request,"docsab/doctor_booking.html",{
            "doctor":doctor_details,
            "slot":slot,
            "patient":patient_name
        })
    
        return render(request,'docsab/about.html')

def booking_confirmation(request,slug1,slug2,slug3):
    doctor=Doctor.objects.get(pk=slug1)
    patient=Patient.objects.get(pk=slug2)
    slot=TimeSlot.objects.get(pk=slug3)
    booking=Booking(
            doctor=doctor,
            patient=patient,
            is_completed=False,
            time_slot=slot
        )
    booking.save()
    subject = 'Hello from Django!'
    message = 'This is a test email sent from Django.'
    from_email = 'hasnain.sohail@arbisoft.com'  # Replace with your Gmail email address
    recipient_list = ['hasnainsohail3030@gmail.com']  # Replace with the recipient's email address

    send_mail(subject, message, from_email, recipient_list)
    return render(request,'docsab/confirm_booking.html')

def all_hospitals(request):
    hosp_list= Hospital.objects.all()
    return render(request,"docsab/all_hospitals.html" ,{
        "hosps":hosp_list
    })

def hospital(request,slug):
    
    hosp_details=Hospital.objects.get(pk=slug)
    #doctor_hospital_list=doctor_details.hospital_set.all()
    return render(request,"docsab/hosp.html",{
        "hosp":hosp_details,
    })


def about(request):
    return render(request,"docsab/about.html" )
