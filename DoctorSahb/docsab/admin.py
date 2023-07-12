from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Address)
admin.site.register(Gender)
admin.site.register(Role)
admin.site.register(User)
admin.site.register(Speciality)
admin.site.register(Doctor)
admin.site.register(Hospital)
admin.site.register(Patient)
admin.site.register(Ratings)
admin.site.register(Booking)
