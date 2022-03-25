from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from home.views import AlunoViewSet, DetailViewSet, CursoViewSet

rotas = routers.DefaultRouter()
rotas.register('aluno', AlunoViewSet, basename='Aluno')
rotas.register('curso', CursoViewSet, basename='Curso')

urlpatterns = [
    path('', include(rotas.urls)),
    path('admin/', admin.site.urls),
    path('aluno/<int:pk>/matricula/', DetailViewSet.as_view())
]
