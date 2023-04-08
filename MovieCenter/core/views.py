from django.shortcuts import render, redirect
from django.http import HttpResponse

#class-based views
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

#models
from core.models import Review

# Create your views here.

#vistas basadas en clases
class Index(ListView):
    model=Review
    template_name='core/index.html'

class LeerReview(DetailView):
    model=Review
    template_name='core/leer_review.html'



#vistas basadas en funciones
def buscar_review(request):
    return render(request, 'core/buscar_review.html')

def resultados_busqueda(request):
    if request.GET['pelicula']:
        pelicula=request.GET['pelicula']
        reviews=Review.objects.filter(pelicula__icontains=pelicula)
        return render(request, 'core/resultado.html', {'reviews':reviews, 'pelicula':pelicula})
    else:
        return redirect('Buscar')