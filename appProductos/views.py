from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.core.mail import send_mail
from django.contrib.auth.views import LoginView
from .models import Producto
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
# Vista para la página de inicio
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.shortcuts import redirect

class CustomLoginView(LoginView):
    template_name = 'login.html'  # Asegúrate de que esta sea la plantilla correcta
    success_url = reverse_lazy('index')  # Redirige a la página principal tras el inicio de sesión

    def form_valid(self, form):
        # Aquí puedes añadir lógica adicional si es necesario
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class IndexView(TemplateView):
    template_name = 'index.html'

def index(request):
    return render(request, 'index.html')

# Vista para mostrar los productos
from django.shortcuts import render
from .models import Producto  # Asegúrate de que este sea el modelo correcto

def productos(request):
    productos = Producto.objects.all()  # Obtén todos los productos de la base de datos
    return render(request, 'productos.html', {'misProductos': productos})

# Vista para la política de privacidad
def privacy_policy(request):
    return render(request, 'sobre.html')

# Vista para la página de contacto
from django import forms

from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            mensaje = form.cleaned_data['mensaje']

            send_mail(
                subject=f'Contacto desde {nombre}',
                message=mensaje,
                from_email=email,
                recipient_list=['destinatario@example.com'],  # Cambia esto por tu dirección de correo
                fail_silently=False,
            )
            return redirect('contact_success')  # Redirige a una página de éxito después de enviar
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


# Vista personalizada para el inicio de sesión
class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True  
    success_url = '/index/'  

    def get_success_url(self):
        return self.success_url

# Vista para manejar la página 404 (opcional)
def test(request):
    return render(request, '404.html')
