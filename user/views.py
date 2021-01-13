from braces.views import LoginRequiredMixin
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django_filters.views import FilterView

from user.filters import ProfileFilter
from user.forms import SignUpForm
from user.models import User, Profile


# Create your views here.
class BasicCreateUserView(CreateView):
    template_name = 'user/criar_user.html'
    form_class = SignUpForm
    model = User

    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('quiz:dashboar')
        else:
            return render(request, 'user/signup.html', {'form': form})


def logged_in(request):
   if request.user.is_superuser:
       return redirect('/api_quiz')
   else:
      return redirect('quiz:dashboar')


# Create your views here.


class ProfileListView(LoginRequiredMixin, FilterView):
    template_name = 'profile/tabela.html'
    model = Profile
    filterset_class = ProfileFilter

    def get_queryset(self):
        queryset = Profile.objects.filter(user__is_superuser=False).order_by('-total_pontos').distinct()
        Profile.att_sequncial(queryset)
        Profile.att_pontuacao(queryset, '', categoria=False)

        return queryset