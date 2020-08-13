from django.contrib.auth.decorators import login_required
from django.conf.urls import url
from .views import *
from django.contrib.auth import views as auth_views

#nome do app
app_name='egressapp'

#array
urlpatterns = [
    url(r'^$',index,name='index'),

    url(r'^sempermissao$',login_required(sempermissao),name='sempermissao'),
    url(r'^relatorios$',login_required(relatorios),name='relatorios'),
    url(r'^esqueceusenha$',esqueceuSenha,name='esqueceuSenha'),

    url(r'^liberar_alunos/$',login_required(liberarAlunos),name='liberarAlunos'),

    url(r'^login',auth_views.login,{'template_name': 'login.html' ,'current_app':'egressapp'},name='login'),
    url(r'^logout',auth_views.logout,{'template_name': 'index.html','current_app':'egressapp'},name='logout'),
    #url(r'^logout',auth_views.logout,{'template_name': 'logout.html','current_app':'egressapp'},name='logout'),

    url(r'^user/update/(?P<pk>[0-9]+)/$',login_required(UserUpdate.as_view()),name='userUpdate'),
    url(r'^user/new/$',login_required(UserCreate.as_view()),name='userNew'),
    url(r'^user/(?P<pk>[0-9]+)/$',login_required(userDetalhes),name='userDetalhes'),
    url(r'^user/$',login_required(user),name='user'),
    url(r'^user/delete/(?P<pk>[0-9]+)/$',login_required(UserDelete.as_view()), name='userDelete'),

    #Url que chama url com id do perfil cooreto pegando o id do user.
    url(r'^perfil/alternativa/(?P<pk>[0-9]+)/$',login_required(perfilAlternativa),name='perfilAlternativa'),

    url(r'^perfil/update/(?P<pk>[0-9]+)/$',login_required(PerfilUpdate.as_view()),name='perfilUpdate'),
    url(r'^perfil/(?P<pk>[0-9]+)/$',login_required(perfilDetalhes),name='perfilDetalhes'),
    url(r'^perfil/$',login_required(perfil),name='perfil'),


    #url(r'^perfil/update/(?P<pk>[0-9]+)/$',login_required(PerfilUpdate.as_view()),name='PerfilUpdate'),


    #url(r'^turmas/new/$',login_required(acesso),name='turmaNew'),#Adicionando nova url
    url(r'^turmas/new/$',login_required(TurmaCreate.as_view()),name='turmaNew'),#Adicionando nova url
    url(r'^turmas/(?P<pk>[0-9]+)/$',login_required(turmaDetalhes),name='turmaDetalhes'),
    url(r'^turmas/$',login_required(turmas),name='turmas'),
    url(r'^turmas/update/(?P<pk>[0-9]+)/$',login_required(TurmaUpdate.as_view()),name='turmaUpdate'),
    url(r'^turmas/delete/(?P<pk>[0-9]+)/$',login_required(TurmaDelete.as_view()), name='turmaDelete'),

    url(r'^alunos/new/$',login_required(AlunoCreate.as_view()),name='alunoNew'),
    url(r'^alunos/(?P<pk>[0-9]+)/$',login_required(alunoDetalhes),name='alunoDetalhes'),
    url(r'^alunos/$',login_required(alunos),name='alunos'),
    url(r'^alunos/update/(?P<pk>[0-9]+)/$',login_required(AlunoUpdate.as_view()),name='alunoUpdate'),
    url(r'^alunos/delete/(?P<pk>[0-9]+)/$',login_required(AlunoDelete.as_view()), name='alunoDelete'),


    url(r'^autorizacao_alunos/new/(?P<pk>[0-9]+)/$',login_required(autorizacaoAlunoCreateEspecifico),name='autorizacaoAlunoEspecificoNew'),
    url(r'^autorizacao_alunos/new/$',login_required(AutorizacaoAlunoCreate.as_view()),name='autorizacaoAlunoNew'),
    url(r'^autorizacao_alunos/(?P<pk>[0-9]+)/$',login_required(autorizacaoAlunoDetalhes),name='autorizacaoAlunoDetalhes'),
    url(r'^autorizacao_alunos/$',login_required(autorizacaoAluno),name='autorizacaoAluno'),
    url(r'^autorizacao_alunos/update/(?P<pk>[0-9]+)/$',login_required(AutorizacaoAlunoUpdate.as_view()),name='autorizacaoAlunoUpdate'),
    url(r'^autorizacao_alunos/delete/(?P<pk>[0-9]+)/$',login_required(AutorizacaoAlunoDelete.as_view()), name='autorizacaoAlunoDelete'),

    url(r'^autorizacao_turmas/new/(?P<pk>[0-9]+)/$',login_required(autorizacaoTurmaCreateEspecifica),name='autorizacaoTurmaEspecificaNew'),
    url(r'^autorizacao_turmas/new/$',login_required(AutorizacaoTurmaCreate.as_view()),name='autorizacaoTurmaNew'),
    url(r'^autorizacao_turmas/(?P<pk>[0-9]+)/$',login_required(autorizacaoTurmaDetalhes),name='autorizacaoTurmaDetalhes'),
    url(r'^autorizacao_turmas/$',login_required(autorizacaoTurma),name='autorizacaoTurma'),
    url(r'^autorizacao_turmas/update/(?P<pk>[0-9]+)/$',login_required(AutorizacaoTurmaUpdate.as_view()),name='autorizacaoTurmaUpdate'),
    url(r'^autorizacao_turmas/delete/(?P<pk>[0-9]+)/$',login_required(AutorizacaoTurmaDelete.as_view()), name='autorizacaoTurmaDelete'),




    #url(r'^alunos/(?P<pk>[0-9]+)/$',alunoDetalhes,name='alunoDetalhes'),
    #url(r'^alunos/$',alunos,name='alunos'),
    #url(r'^alunos/update/(?P<pk>[0-9]+)/$',AlunoUpdate.as_view(),name='alunoUpdate'),
    #url(r'^alunos/delete/(?P<pk>[0-9]+)/$',AlunoDelete.as_view(), name='alunoDelete'),

    #nomear view para usar dantro do html sem a necessidade de aletrar rota, mas chamando pelo nome
    #url(r'^turma/nova/$',TurmaCreate.as_view(),name='CriarUsuario'),
]
