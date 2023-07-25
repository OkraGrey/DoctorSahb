from django import forms
from .models import *

class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        exclude =['hospital','is_completed']
        labels={
            "patient":"Patient Name",
            "doctor":"Doctor Name"
        }
        