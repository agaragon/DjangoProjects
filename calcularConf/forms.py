from django import forms
from calcularConf.models import DadosDasEmpresas
from crispy_forms.helper import FormHelper

class DadosDasEmpresasForm(forms.ModelForm):
    helper = FormHelper()
    
    class Meta:
        model = DadosDasEmpresas
        fields = '__all__'