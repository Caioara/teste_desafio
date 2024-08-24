from django import forms
from .models import Livro

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['isbn', 'titulo', 'autor', 'categoria', 'data_publicacao']
        widgets = {
            'data_publicacao': forms.DateInput(attrs={'type': 'date'}),
        }
