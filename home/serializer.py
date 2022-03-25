from rest_framework import serializers

from home.models import Aluno, Curso, Matricula


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'


class AlunoSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['nome', 'telefone', 'cpf', 'rg', ]


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'


class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = '__all__'


class DetailMatriculaSerializer(serializers.ModelSerializer):
    nome = serializers.ReadOnlyField(source='aluno.nome')
    telefone = serializers.ReadOnlyField(source='aluno.telefone')
    curso_nome = serializers.ReadOnlyField(source='curso.nome_curso')

    class Meta:
        model = Matricula
        fields = ['aluno', 'nome', 'curso', 'creacao', 'curso_nome', 'telefone']
