from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import CustomLoginView
from django.urls import path
from django.views.generic.base import TemplateView 


from django.urls import path
from . import views
from .views import CustomLoginView, IndexView

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),  # Página de inicio de sesión
    path('index/', IndexView.as_view(), name='index'),  # Página principal (index)
    path('productos/', views.productos, name='productos'),
    path('contact/', views.contact, name='contact'),
    path('sobre/', views.privacy_policy, name='sobre'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('contact-success/', TemplateView.as_view(template_name='contact_success.html'), name='contact_success'),  # Página de inicio de sesión (puede ser redundante si ya tienes la ruta en la URL vacía)
]

