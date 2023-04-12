from django.shortcuts import render, redirect
from django.http import HttpResponse

#permisos
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
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

class EditReview(LoginRequiredMixin, UpdateView):
    model=Review
    template_name='core/edit_review.html'
    success_url='/'
    fields=['pelicula', 'titulo', 'texto', 'fecha', 'poster']


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


@login_required
def eliminar_review(request, pk):
    review=Review.objects.get(id=pk)
    if request.user==review.autor:
        review.delete()
        msj=f'Se ha borrado la reseña nro {pk}'
    else:
        msj=f'No se borro la reseña nro {pk} porque usted no la ha escrito.'
    return render(request, 'core/eliminar_review.html', {'msj':msj, 'id':pk})


def about(request):
    return render(request, 'core/about.html')


