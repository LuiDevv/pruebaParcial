from django.urls import path, include
from . import views



urlpatterns = [
    #path('Productos/', views.Productos, name='Productos'),
    path('productos/', views.Productos, name='productos'),
    
    path('index', views.index, name='index'),  # Ruta principal

    path('test/', views.test)
    
]




