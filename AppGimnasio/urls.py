from django.urls import path
from AppGimnasio import views

urlpatterns = [
    path('inicio',views.inicio, name="Inicio"),
    path('musculacion', views.musculacion, name="Musculacion"),
    path('yoga', views.yoga, name="Yoga"),
    path('natacion', views.natacion, name="Natacion"),
    path('musculacionformulario', views.musculacionformulario, name="Musculacionformulario"),
]
