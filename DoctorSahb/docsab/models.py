from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Address(models.Model):
    plot_no = models.CharField(max_length=50)
    street_no = models.CharField(max_length=50)
    town = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    
    def __str__(self):
        return f'{self.plot_no}, {self.street_no}, {self.town}, {self.city}, {self.province} {self.postal_code}'

    class Meta:
        verbose_name_plural= "Address"



class Gender(models.Model):
    gender_type = models.CharField(max_length=10)

    def __str__(self):
        return self.gender_type


class Role(models.Model):
    role_description = models.CharField(max_length=100)

    def __str__(self):
        return self.role_description


# class User(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     contact = models.CharField(max_length=20)
#     role = models.ForeignKey(Role, on_delete=models.CASCADE)
#     address = models.ForeignKey(Address, on_delete=models.CASCADE)
#     gender = models.ForeignKey(Gender, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name


class Speciality(models.Model):
    specialty_description = models.CharField(max_length=100)

    def __str__(self):
        return self.specialty_description
    class Meta:
        verbose_name_plural= "Specialities"


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_surgeon = models.BooleanField(default=False)
    is_available_online = models.BooleanField(default=False)
    cnic = models.CharField(max_length=15)
    consultation_fee = models.DecimalField(max_digits=8, decimal_places=2)
    about = models.TextField()
    speciality = models.OneToOneField(Speciality, on_delete=models.CASCADE)
    address = models.ForeignKey(Address,null=True ,on_delete=models.CASCADE)
    gender = models.ForeignKey(Gender,null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.first_name

class TimeSlot(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='time_slots')
    slot_date = models.DateField(null=True)
    start_time=models.TimeField(null=True)
    end_time = models.TimeField(null=True)
    def __str__(self):
        return self.start_time
class Hospital(models.Model):
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    location_link = models.URLField()
    website_link = models.URLField()
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    hospital_specialities = models.ManyToManyField(Speciality)
    doctors = models.ManyToManyField(Doctor)
    about = models.TextField(null=True)
    def __str__(self):
        return self.name


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    gender = models.ForeignKey(Gender, null=True,on_delete=models.CASCADE)
    contact_number=models.CharField(max_length=12,unique=True,null=True)

    def __str__(self):
        return self.user.first_name

class Ratings(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    doctor = models.OneToOneField(Doctor, on_delete=models.CASCADE)
    rating_value = models.DecimalField(max_digits=2, decimal_places=1)
    rating_date = models.DateTimeField(auto_now_add=True)
    booking = models.OneToOneField('Booking', on_delete=models.CASCADE)

    def __str__(self):
        return f"Rating for {self.doctor.user.name} by {self.patient.user.name}"

    def clean(self):
        if self.rating_value < 0 or self.rating_value > 5 or self.rating_value % 0.5 != 0:
            raise ValidationError("Rating value should be between 0 and 5 with multiples of 0.5.")

class Booking(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    doctor = models.OneToOneField(Doctor, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)
    hospital = models.OneToOneField(Hospital, on_delete=models.CASCADE)
    time_slot= models.OneToOneField(TimeSlot,on_delete=models.CASCADE,null=True,unique=True)
    def __str__(self):
        return f"Booking for {self.doctor.user.first_name} by {self.patient.user.first_name}"
