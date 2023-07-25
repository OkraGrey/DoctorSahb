from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import *
from .forms import *

from django.contrib.auth.views import LoginView
from .models import *

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
    return render(request,"docsab/doctor_slots.html",{
        "doctor":doctor_details,
        "hosps":doctor_hospital_list,
        "slots":doctor_slots,
    })

def doctor_booking(request,slug1,slug2):
    
    slot= TimeSlot.objects.get(pk=slug2)
    doctor_details=Doctor.objects.get(pk=slug1)
    return render(request,"docsab/doctor_booking.html",{
        "doctor":doctor_details,
        "slot":slot,
    })
# def doctor_booking(request,slug1,slug2):
        
#     if request.method == 'POST':
#         form = BookingForm(request.POST)
#         if form.is_valid():
#             # Save the form and redirect on successful form submission
#             form.save()
#             return redirect('success_url_name')
#     else:
#         # If the user is authenticated and validated, populate patient fields
#         if request.user.is_authenticated:
#             try:
#                 patient_instance = request.user
#                 print(request.user)
#                 initial_data = {'patient': patient_instance.pk}
#                 form = BookingForm(initial=initial_data)
#             except Patient.DoesNotExist:
#                 form = BookingForm()
#                 print("caught error")
#         else:
#             form = BookingForm()

#     return render(request, 'docsab/doctor_booking.html', {'form': form})
##########
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
