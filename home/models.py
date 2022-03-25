from django.db import models


class Aluno(models.Model):
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=15)
    cpf = models.CharField(max_length=15)
    rg = models.CharField(max_length=15)

    def __str__(self):
        return self.nome


class Curso(models.Model):
    nome_curso = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome_curso


class Matricula(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.DO_NOTHING)
    curso = models.ForeignKey(Curso, on_delete=models.DO_NOTHING)
    creacao = models.DateTimeField(auto_now_add=True)
    situacao = models.CharField(default='A', max_length=1, choices=(
        ('A', 'Ativo'),
        ('I', 'Inativo'),
        ('C', 'Concluido'),
    ))
