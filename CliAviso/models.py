from django.db import models

class CliAviso(models.Model):

    mensagem = models.CharField(max_length=100)