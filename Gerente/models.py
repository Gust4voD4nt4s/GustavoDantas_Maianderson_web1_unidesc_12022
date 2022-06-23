from django.db import models

class Gerente(models.Model):

    comissao = models.IntegerField(max_length=100)

    def calcular_Salario(self):
        return 0