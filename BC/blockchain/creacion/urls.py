from django.urls import path
from . import views

urlpatterns = [
path('bc', views.procesar),
path('subir', views.subir),
path('vista_val', views.vista_val),
path('validar', views.validar)
]