from django.urls import path

from quiz import views

app_name = 'quiz'

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboar'),
    path('teste/<int:categoria_id>', views.TesteView.as_view(), name='teste'),

    path('lista/', views.CategoriaViewSet.as_view(), name='lista'),
    path('adm/', views.CategoriaAdminViewSet.as_view({'get': 'list'}), name='adm-lista'),
    path('questao/', views.QuestaoAdminViewSet.as_view({'get': 'list'}), name='questao-lista'),

]