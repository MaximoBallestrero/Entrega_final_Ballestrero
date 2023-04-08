from django.contrib import admin
from django.urls import path, include

from core.views import Index, LeerReview, buscar_review, resultados_busqueda

urlpatterns = [
    path('', Index.as_view(), name='Index'),
    path('review/<pk>', LeerReview.as_view(), name='Leer-Review'),
    path('buscar-review/', buscar_review, name='Buscar'),
    path('resultado-busqueda/', resultados_busqueda, name='Resultado'),
]