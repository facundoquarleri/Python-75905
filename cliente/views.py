from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from .models import Pais, Cliente
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import DetailView

def index(request):
    return render(request, 'cliente/index.html')

def pais_list(request):
    paises = Pais.objects.all()
    contexto = {"paises": paises}
    return render(request, 'cliente/pais_list.html', contexto)

def cliente_login(request):
    error = None
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        mail = request.POST.get("mail")
        nacimiento = request.POST.get("nacimiento")
        pais_origen_nombre = request.POST.get("pais_origen")
        pais, created = Pais.objects.get_or_create(nombre=pais_origen_nombre)
        try:
            cliente = Cliente.objects.get(nombre=nombre, apellido=apellido, mail=mail)
            request.session['cliente_id'] = cliente.id
            return redirect('/producto/')
        except Cliente.DoesNotExist:
            cliente = Cliente.objects.create(nombre=nombre, apellido=apellido, mail=mail, nacimiento=nacimiento, pais_origen=pais)
            request.session['cliente_id'] = cliente.id
            return redirect('/producto/')
    return render(request, 'cliente/clientelogin.html', {"error": error})

def is_admin(user):
    return user.is_superuser

@login_required(login_url='/admin/login/')
@user_passes_test(is_admin)
def cliente_list_admin(request):
    clientes = Cliente.objects.all()
    contexto = {"clientes": clientes, "admin": True}
    return render(request, 'cliente/cliente_list.html', contexto)

def cliente_list(request):
    clientes = Cliente.objects.all()
    contexto = {"clientes": clientes, "admin": False}
    return render(request, 'cliente/cliente_list.html', contexto)

def clientedatos(request):
    cliente_id = request.session.get('cliente_id')
    if not cliente_id:
        return redirect('cliente:cliente_login')
    cliente = Cliente.objects.get(id=cliente_id)
    return render(request, 'cliente/clientedatos.html', {'cliente': cliente})

def admin_login(request):
    error = None
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_superuser:
            auth_login(request, user)
            return redirect('cliente:index')
        else:
            error = "Datos incorrectos. Intente de nuevo."
    return render(request, 'cliente/adminlogin.html', {"error": error})

class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'cliente/clientedetail.html'
    context_object_name = 'cliente'