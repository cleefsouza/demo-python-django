from django.db import models

#
#  Classes que representam cliente e suas informações na aplicação
#



class Telefone(models.Model):
    numero = models.CharField(
        max_length=14,
        null=False,
        blank=False
    )

    objetos = models.Manager()


class Endereco(models.Model):
    cep = models.CharField(
        max_length=9,
        null=False,
        blank=False
    )

    rua = models.TextField(
        null=True,
        blank=True
    )

    num = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    bairro = models.TextField(
        null=True,
        blank=True
    )

    cidade = models.TextField(
        null=True,
        blank=True
    )

    uf = models.CharField(
        max_length=2,
        null=True,
        blank=True
    )

    pais = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    objetos = models.Manager()

class Cliente(models.Model):
    nome = models.TextField(
        null=False,
        blank=False
    )

    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE, null=False)
    telefone = models.OneToOneField(Telefone, on_delete=models.CASCADE, null=False)

    objetos = models.Manager()

    def __str__(self):
        return self.nome