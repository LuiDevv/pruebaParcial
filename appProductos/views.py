from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Producto
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.shortcuts import render


def mostrar_template(request):
    return render(request, 'miPrimerTemplate.html')
# Create your views here.

def Productos(request):
    #return HttpResponse("Nuestra primera vista!")
    misProductos = Producto.objects.all().values()

    template = loader.get_template('productos.html')
    context = {
        'misProductos': misProductos,
    }
    return HttpResponse(template.render(context, request))

def BienvenidaProductos(request):
    template = loader.get_template('miPrimerTemplate.html')
    return HttpResponse(template.render())


from django.shortcuts import render

def index(request):
    return render(request, 'index.html')



class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True  
    success_url = '/index/'  

    def get_success_url(self):
        return self.success_url
    

def home(request):
    return render(request, 'home.html')


def privacy_policy(request):
    return render(request, 'privacy_policy.html')


def contact(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']
        from_email = request.POST['email']
        send_mail(subject, message, from_email, ['your_email@example.com'])
        return HttpResponse('Correo enviado con éxito')
    return render(request, 'contact.html')


# def articles_list(request):
    articles = Article.objects.all()
    return render(request, 'articles_list.html', {'articles': articles})


def test(request):
    return render(request, '404.html')
