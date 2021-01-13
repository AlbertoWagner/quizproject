from django.db import models

# Create your models here.
from quiz.choices import CORRETAS


class Categoria(models.Model):
    categoria = models.CharField(verbose_name=("categoria"), max_length=250, blank=True, unique=True, null=True)

    class Meta:
        verbose_name = ("Categoria")
        verbose_name_plural = ("Categoria")

    def __str__(self):
        return self.categoria


class Questao(models.Model):
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    questao = models.CharField(max_length=700, blank=False, null=False, verbose_name='Questão')
    opicao_a = models.CharField(max_length=500, blank=False, null=False, verbose_name='Opicao A')
    opicao_b = models.CharField(max_length=500, blank=False, null=False, verbose_name='Opicao B')
    opicao_c = models.CharField(max_length=500, blank=False, null=False, verbose_name='Opicao C')
    correta = models.CharField(max_length=2, blank=False, null=False, choices=CORRETAS)

    class Meta:
        verbose_name = ("Questão")
        verbose_name_plural = ("Questões")

    def __str__(self):
        return self.questao
