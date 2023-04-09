from django.shortcuts import render, redirect

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from usuarios.forms import UserRegisterForm

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
