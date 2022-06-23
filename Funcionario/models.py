from django.db import models

class Funcionario(models.Model):

    cpf = models.CharField(max_length=100)
    rg = models.CharField(max_length=100)
    nome = models.CharField(max_length=100)
    sexo = models.CharField(max_length=100)
    dataNacimento = models.DateField(max_length=100)
    carteiraTrabalho = models.CharField(max_length=100)
    salario = models.IntegerField(max_length=100)
    pis = models.CharField(max_length=100)

    def consultar_Imoveis(self):
        return 0

    def manter_Anuncio(self):
        return 0

    def manter_Cliene(self):
        return 0

    def manter_Funcionario(self):
        return 0

    def manter_Agendamento(self):
        return 0

    def gerar_Relatorio(self):
        return 0

    def calcular_Salario(self):
        return 0