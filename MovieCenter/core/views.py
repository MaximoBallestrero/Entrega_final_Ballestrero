from django.shortcuts import render

#class-based views
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

#models
from core.models import Review

# Create your views here.
class Index(ListView):
    model=Review
    template_name='core/index.html'

class LeerReview(DetailView):
    model=Review
    template_name='core/leer_review.html'