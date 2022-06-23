from django.db import models

class Locacao(models.Model):

    dataDesocupacao = models.DateField(max_length=100)
    periodo = models.DateField(max_length=100)
    formaGarantida = models.CharField(max_length=100)
    fiador = models.CharField(max_length=100)