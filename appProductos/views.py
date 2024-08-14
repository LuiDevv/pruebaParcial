from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
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

from .models import User

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    
    return redirect('login')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
      
        print(username, password)
        user = User.objects.create_user(username=username, password=password)
        user.save()
        login(request, user)

        return redirect('index')

    return render(request, '404.html')



@method_decorator(login_required, name='dispatch')
class IndexView(TemplateView):
    template_name = 'index.html'

@login_required
def index(request):
    return render(request, 'index.html')

# Vista para mostrar los productos
from django.shortcuts import render
from .models import Producto  # Asegúrate de que este sea el modelo correcto

def productos(request):
    productos = Producto.objects.all()  # Obtén todos los productos de la base de datos
    return render(request, 'productos.html', {'productos': productos})

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
