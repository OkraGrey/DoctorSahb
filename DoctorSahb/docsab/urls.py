from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name="index"),
    path("all_doctors",views.all_doctors, name="all_doctors"),
    path("docsab/<int:slug>",views.doctor,name="doctor-detail"),
]
