from django.contrib import admin
from django.urls import path, include

from core.views import Index, LeerReview

urlpatterns = [
    path('', Index.as_view(), name='Index'),
    path('review/<pk>', LeerReview.as_view(), name='Leer-Review')
]