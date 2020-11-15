from django import forms
from core.models import Computadora

class ComputadoraForm(forms.ModelForm):
    class Meta:
        model = Computadora
        fields = "__all__"