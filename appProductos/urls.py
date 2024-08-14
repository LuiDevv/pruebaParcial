from django.urls import path
from . import views
from .views import CustomLoginView, IndexView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),  # Página de inicio de sesión
    path('', IndexView.as_view(), name='index'),  # Página principal (index)
    path('productos/', views.productos, name='productos'),
    path('contact/', views.contact, name='contact'),
    path('sobre/', views.privacy_policy, name='sobre'),
    # path('login/', CustomLoginView.as_view(), name='login'),  # Esta línea puede ser redundante
]
