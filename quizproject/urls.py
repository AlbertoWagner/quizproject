"""quizproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

# Rotas dos apps
from quiz.views import CategoriaAdminViewSet, QuestaoAdminViewSet

api_router = routers.DefaultRouter()
api_router.register(r"categoria", CategoriaAdminViewSet)
api_router.register(r"questao", QuestaoAdminViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user.urls')),
    path('api_quiz/', include(api_router.urls)),
    path('quiz/', include('quiz.urls')),

]




