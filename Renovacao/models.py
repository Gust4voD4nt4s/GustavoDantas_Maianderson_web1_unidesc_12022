from django.db import models

class Renovacao(models.Model):

    dataDesocupacao = models.DateField(max_length=100)
    dataRenovacao = models.DateField(max_length=100)
    cartorio = models.CharField(max_length=100)
