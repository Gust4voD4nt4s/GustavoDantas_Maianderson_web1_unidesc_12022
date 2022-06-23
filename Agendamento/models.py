from django.db import models

class Agendamento(models.Model):

    dia = models.DateField(max_length=100)
    hora = models.TimeField(max_length=100)
    local = models.CharField(max_length=100)

    def incuir_Agendamento(self):
        return 0
    def consultar_Agendamento(self):
        return 0
    def alterar_Agendamento(self):
        return 0

    def remover_Agendamento(self):
        return 0