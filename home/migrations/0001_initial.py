# Generated by Django 4.0.3 on 2022-03-17 21:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('telefone', models.CharField(max_length=15)),
                ('cpf', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_curso', models.CharField(max_length=50)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creacao', models.DateTimeField(auto_now_add=True)),
                ('situacao', models.CharField(choices=[('A', 'Ativo'), ('I', 'Inativo'), ('C', 'Concluido')], default='A', max_length=1)),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='home.aluno')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='home.curso')),
            ],
        ),
    ]
