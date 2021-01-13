from django.contrib.auth.models import User
from django.db.models.signals import post_save

from quiz.models import Questao

from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_pontos = models.IntegerField(blank=True, default=0)
    sequencial = models.IntegerField(blank=True, default=1)
    questao_corretas = models.ManyToManyField(Questao, related_name='questao_corretas', blank=True)
    questao_erradas = models.ManyToManyField(Questao, related_name='questao_erradas', blank=True)
    pontos = models.IntegerField(blank=True, default=0)

    def adicionar_pontos(self):
        self.total_pontos += 1
        self.save()

    def remove_pontos(self):
        if self.total_pontos != 0:
            self.total_pontos -= 1
            self.save()

    def att_sequncial(queryset):
        sequencial = 1
        for item in queryset:
            print(queryset)
            item.sequencial = sequencial
            item.save()
            sequencial += 1

    def soma_de_pontos(soma):
        if soma >= 0:
            return soma
        else:
            return 0

    def att_pontuacao(lista_profile, id, categoria=False):
        for item in lista_profile:
            pontos_q_certas = Profile.objects.filter(questao_corretas__categoria__id__in=id, user=item.user).count()
            pontos_q_erradas = Profile.objects.filter(questao_erradas__categoria__id__in=id, user=item.user).count()
            soma = pontos_q_certas - pontos_q_erradas
            print(soma)
            if categoria:
                item.pontos = Profile.soma_de_pontos(soma)
                item.save()
            else:
                item.pontos = item.total_pontos
                item.save()


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


post_save.connect(create_user_profile, sender=User)
