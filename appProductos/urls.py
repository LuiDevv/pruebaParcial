from django.urls import path, include
from . import views
from .views import CustomLoginView



urlpatterns = [
    #path('Productos/', views.Productos, name='Productos'),
    path('productos/', views.Productos, name='productos'),
    
    path('index/', views.index, name='index'), 

    path('test/', views.test),

    path('', CustomLoginView.as_view(), name='login'),
    
    path('index/', views.index, name='index')
    
]




