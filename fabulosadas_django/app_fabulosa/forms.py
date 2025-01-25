from django import forms
from .models import PropRetos, SendRetos

class FormRetos(forms.Form):
    class Meta:
        model = PropRetos
        fields = [
            'name',
            'gmail',
            'description',
            'reto_name',
            'difficulty',
        ]