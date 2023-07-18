from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import *
# Create your views here.

from .models import *

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
