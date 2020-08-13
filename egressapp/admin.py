from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register({Turma,Aluno,AutorizacaoAluno,AutorizacaoTurma,Perfil})#para o admin reconhecer suas classes
