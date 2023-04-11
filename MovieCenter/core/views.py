from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

#class-based views
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

#models
from core.models import Review
from django.contrib.auth.models import User

#forms
from core.forms import ReviewForm

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


@login_required
def crear_review(request):
    if request.method=='POST':
        form=ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            u=User.objects.get(username=request.user)
            review=Review(pelicula=form.cleaned_data['pelicula'],
                        titulo=form.cleaned_data['titulo'],
                        texto=form.cleaned_data['texto'],
                        fecha=form.cleaned_data['fecha'],
                        poster=form.cleaned_data['poster'],
                        autor=u)
            review.save()
            return redirect('Index')
    else:
        form=ReviewForm()
    return render(request, 'core/crear_review.html', {'form':form})