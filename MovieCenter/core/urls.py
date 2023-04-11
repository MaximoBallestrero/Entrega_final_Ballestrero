from django.contrib import admin
from django.urls import path, include

from core.views import Index, LeerReview, buscar_review, resultados_busqueda, crear_review, EditReview, eliminar_review

urlpatterns = [
    path('', Index.as_view(), name='Index'),
    path('review/<pk>', LeerReview.as_view(), name='Leer-Review'),
    path('buscar-review/', buscar_review, name='Buscar'),
    path('resultado-busqueda/', resultados_busqueda, name='Resultado'),
    path('crear-review/', crear_review, name='Crear-Review'),
    path('edit-review/<pk>', EditReview.as_view(), name='Edit-Review'),
    path('eliminar-review/<pk>', eliminar_review, name='Eliminar-Review')
]