from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    password1=forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2=forms.CharField(label='Repita la contraseña', widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=['username', 'email','password1', 'password2']
        help_texts={k:"" for k in fields}


class UserEditForm(forms.Form):
    email=forms.EmailField(label='Modificar mail')
    bio=forms.CharField(label='Modificar descripcion', widget=forms.Textarea)
    avatar=forms.ImageField(label='Modificar avatar')