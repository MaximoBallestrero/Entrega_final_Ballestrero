from django.urls import path

from usuarios.views import login_request, register

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_request, name='Login'),
    path('logout/', LogoutView.as_view(template_name='usuarios/logout.html'), name='Logout'),
    path('register/', register, name='Register')
]