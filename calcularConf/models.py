from django.db import models

# Create your models here.

class Empresa(models.Model):
    nomeDaEmpresa = models.CharField(max_length=128)
    qtdDeNotasEmitidas = models.PositiveIntegerField()
    qtdDePendencias = models.PositiveIntegerField()
    indiceDeConf = models.PositiveIntegerField()
    idDaEmpresa = models.CharField(unique=True,max_length=20)
    def __str__(self):
        return self.nomeDaEmpresa