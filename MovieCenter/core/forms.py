from django import forms

class ReviewForm(forms.Form):
    pelicula=forms.CharField(max_length=40)
    titulo=forms.CharField(max_length=80)
    texto=forms.CharField(widget=forms.Textarea)
    fecha=forms.DateField()
    poster=forms.ImageField()
