from django import forms
from .models import Pedido


class DatosEnvioForm(forms.Form):
    """Formulario para datos de envío y checkout"""
    nombre = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'})
    )
    apellidos = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellidos'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email@ejemplo.com'})
    )
    telefono = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+34 600 000 000'})
    )
    direccion = forms.CharField(
        max_length=300,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Calle, número, piso'})
    )
    ciudad = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ciudad'})
    )
    codigo_postal = forms.CharField(
        max_length=10,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Código Postal'})
    )
    metodo_pago = forms.ChoiceField(
        choices=Pedido.METODO_PAGO_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'})
    )
    notas = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control', 
            'rows': 3,
            'placeholder': 'Notas adicionales sobre tu pedido (opcional)'
        })
    )
