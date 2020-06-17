from django import forms
from calcularConf.models import InfoDasEmpresas


class InfoDasEmpresasForm(forms.ModelForm):
    class Meta:
        model = InfoDasEmpresas
        fields = '__all__'