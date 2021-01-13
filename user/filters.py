import django_filters
from django import forms

from quiz.models import Categoria
from user.models import Profile


class ProfileFilter(django_filters.FilterSet):
    categoria = django_filters.ModelMultipleChoiceFilter(queryset=Categoria.objects.all(),
                                                         widget=forms.CheckboxSelectMultiple,
                                                         method='filter_categoria')

    class Meta:
        model = Profile
        fields = ('user',)

    def filter_categoria(self, queryset, name, value):
        if value is not None:
            queryset = Profile.objects.filter(questao_corretas__categoria__id__in=[item.id for item in value]).order_by('-total_pontos','user__username').distinct()
            Profile.att_sequncial(queryset)
            Profile.att_pontuacao(queryset,[item.id for item in value],categoria=True)
        return queryset
