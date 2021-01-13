from rest_framework import serializers

from quiz.models import Categoria, Questao


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id', 'url', 'categoria')


class QuestaoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Questao
        fields = ('id', 'url', 'categoria', 'questao', 'opicao_a', 'opicao_b', 'opicao_c', 'correta')
