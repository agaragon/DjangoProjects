from django.db import models
from calcularConf.static.rotinas.validators import file_size
from django.core.validators import FileExtensionValidator

# Create your models here.
class Empresa(models.Model):
    nomeDaEmpresa = models.CharField(max_length=128)
    qtdDeNotasEmitidas = models.PositiveIntegerField()
    qtdDePendencias = models.PositiveIntegerField()
    indiceDeConf = models.PositiveIntegerField()
    def __str__(self):
        return self.nomeDaEmpresa

class InfoDasEmpresas(models.Model):
    arquivo = models.FileField(validators=[FileExtensionValidator(allowed_extensions=['json']),file_size])
    empresa = models.ForeignKey(Empresa,on_delete=models.CASCADE)
    