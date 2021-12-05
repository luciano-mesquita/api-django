from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=50)
    idade = models.IntegerField()

    def __str__(self):
        return self.nome


class Veiculo(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)

    def __str__(self):
        return self.marca