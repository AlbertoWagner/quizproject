from braces.views import LoginRequiredMixin, SuperuserRequiredMixin
# Create your views here.
from django.views.generic import TemplateView
from rest_framework import viewsets, generics

from quiz.forms import QuizForm
from quiz.models import Categoria, Questao
from quiz.serializer import CategoriaSerializer, QuestaoSerializer
from user.models import Profile


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'quiz/categoria_list.html'
    model = Categoria

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['categoria_list'] = Categoria.objects.all()
        return context

class TesteView(LoginRequiredMixin, TemplateView):
    template_name = 'quiz/teste.html'
    model = Questao

    def get_questoes(self):
        profile = Profile.objects.get(user=self.request.user)
        questoes = Questao.objects.filter(categoria__id=self.kwargs['categoria_id']).exclude(questao__in=[item.questao for item in profile.questao_corretas.all()]).order_by('?')[0:10]
        return questoes

    def get_context_data(self, **kwargs):
        form = QuizForm(None, questoes=self.get_questoes())

        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        form = QuizForm(self.request.POST, questoes=self.get_questoes())
        profile_user = Profile.objects.get(user=request.user)

        if form.is_valid():
            questions_list = []
            answers_list = []
            for (quiz_question, answer) in form.answers():
                questao = Questao.objects.filter(questao=quiz_question)[0]
                if questao.correta == answer:
                    profile_user.adicionar_pontos()
                    profile_user.questao_corretas.add(questao)
                else:
                    profile_user.remove_pontos()
                    profile_user.questao_erradas.add(questao)

            flag = True

        # if flag:
        #     request.session.clear()
        #     return redirect('finish')
        # # content = zip(questions, form)
        # # request.session['questions'] = id_list
        # context = {'content': 'content'}
        # return render(request, 'quiz.html', context)

        return self.get(request, *args, **kwargs)


class CategoriaViewSet(LoginRequiredMixin, generics.ListAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class CategoriaAdminViewSet(LoginRequiredMixin, SuperuserRequiredMixin, viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    filterset_fields = ['categoria']


class QuestaoAdminViewSet(LoginRequiredMixin, SuperuserRequiredMixin, viewsets.ModelViewSet):
    queryset = Questao.objects.all()
    serializer_class = QuestaoSerializer
    filterset_fields = ['categoria']


# class CategoriaAdminDetailsView(LoginRequiredMixin, SuperuserRequiredMixin, viewsets.ModelViewSet):
#     queryset = Categoria.objects.all()
#     serializer_class = CategoriaSerializer
#     filterset_fields = ['categoria']

#
# class CategoriaViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
#     queryset = Categoria.objects.all()
#     serializer_class = CategoriaSerializer


# class CategoriaQuizViewSet(LoginRequiredMixin, viewsets.ViewSet):
#     queryset = Categoria.objects.all()
#     serializer_class = CategoriaSerializer
#     template_name = 'quiz/categoria_list.html'
#
#     def list(self, request):
#         serializer = CategoriaSerializer()
#         return JsonResponse(serializer.data)
