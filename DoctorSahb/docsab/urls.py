from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name="index"),
    path("all_doctors",views.all_doctors, name="all_doctors"),
    path("docsab/doc/<int:slug>",views.doctor,name="doctor-detail"),
    path("all_hospitals",views.all_hospitals,name="all_hospitals"),
    path("docsab/hosp/<int:slug>",views.doctor,name="hosp-detail"),

]
