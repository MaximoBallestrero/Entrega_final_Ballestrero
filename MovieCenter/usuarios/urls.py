from django.urls import path

from usuarios.views import login_request, register, tu_perfil, edit_perfil


from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_request, name='Login'),
    path('logout/', LogoutView.as_view(template_name='usuarios/logout.html'), name='Logout'),
    path('register/', register, name='Register'),
    path('tu-perfil/', tu_perfil, name='Tu-Perfil'),
    path('editar-perfil/', edit_perfil, name='Editar-Perfil')
]