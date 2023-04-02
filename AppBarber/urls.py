from django.urls import path
from AppBarber.views import sacar_turno
from AppBarber import views
from AppBarber.views import *


urlpatterns = [
    path('inicio/', sacar_turno),
]