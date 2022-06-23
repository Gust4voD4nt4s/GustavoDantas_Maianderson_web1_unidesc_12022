from django.db import models

class Cliente(models.Model):

    dataCadastro = models.DateField(max_length=100)

    def consultar_Imoveis(self):
        return 0

    def manter_Conta(self):
        return 0

    def agendar_Visita(self):
        return 0