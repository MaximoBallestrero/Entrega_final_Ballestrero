from django.shortcuts import render, redirect

from django.views.generic.detail import DetailView

#permisos de django
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

#mis forms
from usuarios.forms import UserRegisterForm, UserEditForm

#models
from core.models import Review 
from usuarios.models import Avatar, DescripcionUsuario


# Create your views here.

def login_request(request):
    mensaje=''
    if request.method=='POST':
        form=AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario=form.cleaned_data.get('username')
            contra=form.cleaned_data.get('password')

            user=authenticate(username=usuario, password=contra)

            if user is not None:
                login(request, user)
                return redirect('Index')

            else:
                mensaje='Error: datos incorrectos'
        else:
            mensaje='Error: datos y/o formulario incorrectos'
    form=AuthenticationForm()
    return render(request, 'usuarios/login.html', {'form':form, 'msj':mensaje})


#el logout es una vista basada en clases que ya esta hecha por django


def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('Index')
    else:
        form=UserRegisterForm()
    return render(request, 'usuarios/register.html', {'form':form})


@login_required
def tu_perfil(request):
    tus_reviews=Review.objects.filter(autor=request.user)
    return render(request, 'usuarios/tu_perfil.html', {'tus_reviews':tus_reviews})


@login_required
def edit_perfil(request):
    usuario=request.user
    try:
        desc=request.user.descripcionusuario.bio
    except:
        desc=DescripcionUsuario(user=usuario, bio='Contanos un poco de vos')
    try:
        avatar=request.user.avatar.imagen
    except:
        avatar=Avatar()
    
    if request.method=='POST':
        form=UserEditForm(request.POST, request.FILES)

        if form.is_valid():
            info=form.cleaned_data
            usuario.email=info['email']
            desc=DescripcionUsuario(user=usuario, bio=info['bio'])
            avatar=Avatar(user=usuario,imagen=info['avatar'])
            usuario.save()
            desc.save()
            avatar.save()
            return redirect('Tu-Perfil')
    else:
        form=UserEditForm(initial={'email':usuario.email, 'bio':desc, 'avatar':avatar})
    return render(request, 'usuarios/editar_perfil.html', {'form':form, 'usuario':usuario})



def get_perfil(request, pk):
    usuario=User.objects.get(id=pk)
    email=usuario.email
    avatar=Avatar.objects.filter(user=pk)
    bio=DescripcionUsuario.objects.filter(user=pk)
    reviews=Review.objects.filter(autor=pk)
    return render(request, 'usuarios/get_perfil.html', {'usuario':usuario, "email":email, "avatar":avatar[0].imagen.url, "bio":bio[0], "reviews":reviews})


