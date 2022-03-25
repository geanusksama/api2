from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from home.models import Aluno, Matricula, Curso
from home.serializer import (
    AlunoSerializer, CursoSerializer,
    MatriculaSerializer, DetailMatriculaSerializer,
    AlunoSerializerV2
)


class AlunoViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Aluno.objects.order_by('-id')

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return AlunoSerializerV2
        else:
            return AlunoSerializer


class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer


class DetailViewSet(generics.ListAPIView):
    def get_queryset(self):
        queryset = Matricula.objects.filter(
            aluno_id=self.kwargs['pk']
        )
        return queryset

    serializer_class = DetailMatriculaSerializer
