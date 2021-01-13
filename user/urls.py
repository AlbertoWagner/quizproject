from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.urls import path
from django.urls import reverse_lazy

from . import views

app_name = 'user'

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('home/', views.logged_in, name="logged_in"),

    path('criar_user/', views.BasicCreateUserView.as_view(), name='criar-user'),
    path('profile/', views.ProfileListView.as_view(), name='profile'),

    # path('home/', views.Home.as_view(), name='home'),
    # path('delete/', views.BasicDeleteUser.as_view(), name='delete'),

    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^reset/$',
        auth_views.PasswordResetView.as_view(
            template_name='user/redefinir_senha.html',
            email_template_name='user/password_reset_email.html',
            subject_template_name='user/password_reset_subject.txt',
            success_url=reverse_lazy('user:password_reset_done')
        ),
        name='password_reset'),
    url(r'^reset/done/$',
        auth_views.PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'),
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        auth_views.PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html',
                                                    success_url=reverse_lazy('user:login')),
        name='password_reset_confirm'),
    url(r'^reset/complete/$',
        auth_views.PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'),
        name='password_reset_complete'),
    url(r'^settings/password/$', auth_views.PasswordChangeView.as_view(template_name='user/password_change.html',
                                                                       success_url=reverse_lazy('user:login')),
        name='password_change'),
    url(r'^settings/password/done/$',
        auth_views.PasswordChangeDoneView.as_view(template_name='user/password_change_done.html', ),
        name='password_change_done'),

]
