from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Conversacion, Mensaje
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models import Count


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('chat')
        else:
            return render(request, 'app_chat/login.html', {'error': 'Usuario o contraseña inválidos'})
    return render(request, 'app_chat/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

#def welcome_view(request):
#    if not request.user.is_authenticated:
#        return redirect('login')
#    return render(request, 'app_chat/welcome.html')

'''
@login_required
def chat_view(request):
    if request.method == "POST" and 'usuario_id' in request.POST:
        usuario_id = request.POST.get('usuario_id')
        otro_usuario = get_object_or_404(User, pk=usuario_id)
        conversacion, created = Conversacion.objects.get_or_create(participantes__in=[request.user, otro_usuario])
        conversacion.participantes.add(request.user, otro_usuario)
        return redirect('conversacion', conversacion_id=conversacion.pk)
    usuarios = User.objects.exclude(id=request.user.id)
    return render(request, 'app_chat/chat.html', {'usuarios': usuarios})
'''

@login_required
def chat_view(request):
    if request.method == "POST" and 'usuario_id' in request.POST:
        usuario_id = request.POST.get('usuario_id')
        otro_usuario = get_object_or_404(User, pk=usuario_id)

        # Verifica si ya existe una conversación entre los dos usuarios
        conversacion = Conversacion.objects.filter(
            participantes__in=[request.user, otro_usuario]
        ).annotate(num_participantes=Count('participantes')).filter(num_participantes=2).first()

        if conversacion is None:
            # Si no existe, entonces crea una nueva conversación
            conversacion = Conversacion.objects.create()
            conversacion.participantes.add(request.user, otro_usuario)

        return redirect('conversacion', conversacion_id=conversacion.pk)

    usuarios = User.objects.exclude(id=request.user.id)
    return render(request, 'app_chat/chat.html', {'usuarios': usuarios})

@login_required
def conversacion_view(request, conversacion_id):
    conversacion = get_object_or_404(Conversacion, pk=conversacion_id, participantes=request.user)
    if request.method == "POST" and 'mensaje' in request.POST:
        mensaje = request.POST.get('mensaje')
        Mensaje.objects.create(conversacion=conversacion, autor=request.user, mensaje=mensaje)
        return redirect('conversacion', conversacion_id=conversacion.pk)
    mensajes = conversacion.mensajes.all()
    return render(request, 'app_chat/conversacion.html', {'conversacion': conversacion, 'mensajes': mensajes})

