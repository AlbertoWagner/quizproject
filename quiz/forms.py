
from crispy_forms.helper import FormHelper
from django import forms
from django.forms import widgets


class QuizForm(forms.Form):

    def __init__(self, *args, **kwargs):
        questoes = kwargs.pop('questoes')  # pop questoes array from kwargs
        super().__init__(*args, **kwargs)
        if questoes:
            for questao in questoes:  # add a form field for each questao
                CHOICES = (
                    ('A', questao.opicao_a),
                    ('B', questao.opicao_b),
                    ('C', questao.opicao_c),
                )
                self.fields[questao.questao] = forms.ChoiceField(required=False, choices=CHOICES,
                                                                           widget=widgets.RadioSelect)
        self.helper = FormHelper()
        self.helper.form_show_labels = False

    def answers(self):  # return questaos and answers for result processing
        for name, questao in self.cleaned_data.items():
            yield (name, questao)
