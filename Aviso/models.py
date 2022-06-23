from django.db import models

class Aviso(models.Model):

    matricula = models.IntegerField(max_length=100)
    assunto = models.CharField(max_length=100)
    data = models.DateField(max_length=100)

    def incluir_Aviso(self):
        return 0

    def consultar_Aviso(self):
        return 0

    def remover_Aviso(self):
        return 0