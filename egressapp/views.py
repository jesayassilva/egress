from django.contrib.auth.forms import  UserCreationForm,AuthenticationForm,UserChangeForm,PasswordResetForm
from django.views.generic.edit import DeleteView,CreateView,UpdateView
from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import datetime, timedelta
from .models import *
#from .forms import *
import datetime
from django.contrib.auth.models import User
# Create your views here.
from django.views.generic.edit import CreateView
from .models import *

'''
    gerenciar_Liberacao_Alunos = models.BooleanField(default = True)
    gerenciar_Alunos = models.BooleanField(default = False)
    gerenciar_Turmas = models.BooleanField(default = False)
    gerenciar_Autorizacao_Turmas = models.BooleanField(default = False)
    gerenciar_Autorizacao_Alunos = models.BooleanField(default = False)
    gerenciar_Relatorios = models.BooleanField(default = False)
    gerenciar_Usuarios = models.BooleanField(default = False)
    gerenciar_Permissoes_Usuarios = models.BooleanField(default = False)

'''


#Pagina Inicial
def index(request):
    #usuario = Aluno.objects.get(id=12)
    usuario = request.user
    #return HttpResponse(usuario)
    return render(request,'index.html',{'usuario':usuario})

#pagina de sem permissao
def sempermissao(request):
    #usuario = Aluno.objects.get(id=12)
    usuario = request.user
    #return HttpResponse(usuario)
    return render(request,'sempermissao.html',{'usuario':usuario})

def esqueceuSenha(request):
    return render(request,'esqueceusenha.html')


def relatorios(request):
    if not request.user.perfil.gerenciar_Relatorios:
        return redirect('/sempermissao')
    #data_hora_maxima = datetime.now() + timedelta(minutes=60)
    #Entry.objects.filter(id__gt=4)
    #return HttpResponse(datetime.now())
    #liberacao = AutorizacaoAluno.objects.filter(aluno__cpf = cpf).filter( data__gt = data_hora_minima ).filter( data__lte = data_hora_maxima )
    alunos_7 = AutorizacaoAluno.objects.filter( data__gt = (datetime.now() - timedelta(days=7)) ).count
    alunos_15 = AutorizacaoAluno.objects.filter( data__gt = (datetime.now() - timedelta(days=15)) ).count
    alunos_30 = AutorizacaoAluno.objects.filter( data__gt = (datetime.now() - timedelta(days=30)) ).count
    alunos_60 = AutorizacaoAluno.objects.filter( data__gt = (datetime.now() - timedelta(days=60)) ).count
    alunos_120 = AutorizacaoAluno.objects.filter( data__gt = (datetime.now() - timedelta(days=120)) ).count
    alunos_180 = AutorizacaoAluno.objects.filter( data__gt = (datetime.now() - timedelta(days=180)) ).count
    alunos_365 = AutorizacaoAluno.objects.filter( data__gt = (datetime.now() - timedelta(days=365)) ).count

    turmas_7 = AutorizacaoTurma.objects.filter( data__gt = (datetime.now() - timedelta(days=7)) ).count
    turmas_15 = AutorizacaoTurma.objects.filter( data__gt = (datetime.now() - timedelta(days=15)) ).count
    turmas_30 = AutorizacaoTurma.objects.filter( data__gt = (datetime.now() - timedelta(days=30)) ).count
    turmas_60 = AutorizacaoTurma.objects.filter( data__gt = (datetime.now() - timedelta(days=60)) ).count
    turmas_120 = AutorizacaoTurma.objects.filter( data__gt = (datetime.now() - timedelta(days=120)) ).count
    turmas_180 = AutorizacaoTurma.objects.filter( data__gt = (datetime.now() - timedelta(days=180)) ).count
    turmas_365 = AutorizacaoTurma.objects.filter( data__gt = (datetime.now() - timedelta(days=365)) ).count

    return render(request,'relatorios.html',{'alunos_7':alunos_7,'alunos_15':alunos_15,'alunos_30':alunos_30,'alunos_60':alunos_60,'alunos_120':alunos_120,'alunos_180':alunos_180,'alunos_365':alunos_365,'turmas_7':turmas_7,'turmas_15':turmas_15,'turmas_30':turmas_30,'turmas_60':turmas_60,'turmas_120':turmas_120,'turmas_180':turmas_180,'turmas_365':turmas_365})



#Liberar Aluno
def liberarAlunos(request):
    #if request.user:
    #    tes = " "
    if not request.user.perfil.gerenciar_Liberacao_Alunos:
        return redirect('/sempermissao')
    exibir = 0
    linhas = 0
    liberacao = ""
    nome_aluno = ""
    # 0 primeiro acesso a pagina
    if  request.method == "POST":
        cpf = request.POST.get("name_cpf")
        cpf = cpf.replace('.', '')
        cpf = cpf.replace('-', '')
        # como substituir palavras ex: test = test.replace('simple', 'short')
        #'exp': datetime.datetime.now() + datetime.timedelta(minutes=60),
        data_hora_minima = datetime.now() - timedelta(minutes=60)
        data_hora_maxima = datetime.now() + timedelta(minutes=60)
        #Entry.objects.filter(id__gt=4)
        #return HttpResponse(datetime.now())
        liberacao = AutorizacaoAluno.objects.filter(aluno__cpf = cpf).filter( data__gt = data_hora_minima ).filter( data__lte = data_hora_maxima )
        linhas = liberacao.count
        if not liberacao:
            data_hora_minima = datetime.now() - timedelta(minutes=60)
            data_hora_maxima = datetime.now() + timedelta(minutes=60)
            #Entry.objects.filter(id__gt=4)
            #return HttpResponse(datetime.now())
            #Perfil.objects.get(user=item.receptor.pk).tipo_usuario == "Pessoa Jurídica"
            #aluno = Aluno.objects.get(cpf=cpf)
            aluno = Aluno.objects.filter(cpf=cpf)
            linhas = aluno.count
            turma_aluno = ""
            if not aluno:
                exibir = 4 #aluno nao encontrado
                return render(request,'liberarAlunos.html',{'liberacao':liberacao,'exibir':exibir})
            for aluno in aluno:
                turma_aluno = aluno.turma
                nome_aluno = aluno.nome
            liberacao = AutorizacaoTurma.objects.filter(turma = turma_aluno ).filter( data__gt = data_hora_minima ).filter( data__lte = data_hora_maxima )
            linhas = liberacao.count
            if not liberacao:
                exibir = 3
                #nao autorizado a sair
            else:
                exibir = 2
                #turma autorizado
        else:
            exibir = 1
            # aluno autorizado a sair
    return render(request,'liberarAlunos.html',{'liberacao':liberacao,'exibir':exibir,'linhas':linhas,'nome_aluno':nome_aluno})

############## Usuario #######################
class UserCreate(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'novo_usuario.html'
    success_url = '/user/'

    def get(self, request, *args, **kwargs):
        if not self.request.user.perfil.gerenciar_Usuarios:
            return redirect('/sempermissao')
        return super(UserCreate, self).get(request, *args, **kwargs)


class UserUpdate(UpdateView):
    model = User
    form_class = UserCreationForm
    #form_class = ProvaForm
    success_url = '/'
    template_name = 'update.html'

    def get(self, request, *args, **kwargs):
        if not self.request.user.perfil.gerenciar_Usuarios:
            return redirect('/sempermissao')
        return super(UserUpdate, self).get(request, *args, **kwargs)


class UserDelete(DeleteView):
    model = User
    success_url = '/user/'
    template_name = 'deleteUser.html'

    def get(self, request, *args, **kwargs):
        if not self.request.user.perfil.gerenciar_Usuarios:
            return redirect('/sempermissao')
        return super(UserDelete, self).get(request, *args, **kwargs)


def user(request):
    if not request.user.perfil.gerenciar_Usuarios:
        return redirect('/sempermissao')
    user = User.objects.all().order_by('username')
    return render(request,'usuarios.html',{'user':user})

def userDetalhes(request,pk):
    if not request.user.perfil.gerenciar_Usuarios:
        return redirect('/sempermissao')
    user = User.objects.get(pk=pk)
    return render(request,'usuarios_detalhes.html',{'user':user})




############## Perfil #######################
#Rota recebe id do user e redireciona para a rota de alterar perfil do usuario
def perfilAlternativa(request,pk):
    if not request.user.perfil.gerenciar_Permissoes_Usuarios:
        return redirect('/sempermissao')
    perfil = Perfil.objects.get(user__pk=pk)
    return redirect('/perfil/update/'+str(perfil.pk)+'/')

class PerfilUpdate(UpdateView):
    model = Perfil
    fields = '__all__'#quais atributos(todos)
    #form_class = ProvaForm
    success_url = '/perfil/'
    template_name = 'update_permissoes.html'

    def get(self, request, *args, **kwargs):
        if not self.request.user.perfil.gerenciar_Permissoes_Usuarios:
            return redirect('/sempermissao')
        return super(PerfilUpdate, self).get(request, *args, **kwargs)


def perfil(request):
    #if ver
    if not request.user.perfil.gerenciar_Permissoes_Usuarios:
        return redirect('/sempermissao')
    perfil = Perfil.objects.all().order_by('user__username')
    return render(request,'perfil.html',{'perfil':perfil})

def perfilDetalhes(request,pk):
    if not request.user.perfil.gerenciar_Permissoes_Usuarios:
        return redirect('/sempermissao')
    perfil = Perfil.objects.get(pk=pk)
    return render(request,'perfil_detalhes.html',{'perfil':perfil})

#doacoes = Doacao.objects.filter(conclusao = False, receptor = None, produto__nome__contains = dados["nome_produto"] ).order_by('data_criacao')
#os dados q vao para os templates
#Turma
############## Turma #######################
class TurmaCreate(CreateView):
    model = Turma#modelos usados
    fields = '__all__'#quais atributos(todos)
    template_name = 'nova_turma.html'#qual templete vai chamar
    success_url = '/turmas/' #qual url vai redirecionar

    def get(self, request, *args, **kwargs):
        if not self.request.user.perfil.gerenciar_Turmas:
            return redirect('/sempermissao')
        return super(TurmaCreate, self).get(request, *args, **kwargs)



def turmas(request):
    if not request.user.perfil.gerenciar_Turmas:
        return redirect('/sempermissao')
    turmas = Turma.objects.all().order_by('nome')
    return render(request,'turmas.html',{'turmas':turmas})

def turmaDetalhes(request,pk):
    if not request.user.perfil.gerenciar_Turmas:
        return redirect('/sempermissao')
    turma = Turma.objects.get(pk=pk)
    return render(request,'turmaDetalhes.html',{'turma':turma})

class TurmaUpdate(UpdateView):
    model = Turma
    fields = '__all__'#quais atributos(todos)
    #form_class = ProvaForm
    success_url = '/turmas/'
    template_name = 'update.html'

    def get(self, request, *args, **kwargs):
        if not self.request.user.perfil.gerenciar_Turmas:
            return redirect('/sempermissao')
        return super(TurmaUpdate, self).get(request, *args, **kwargs)

class TurmaDelete(DeleteView):
    model = Turma
    success_url = '/turmas/'
    template_name = 'delete.html'

    def get(self, request, *args, **kwargs):
        if not self.request.user.perfil.gerenciar_Turmas:
            return redirect('/sempermissao')
        return super(TurmaDelete, self).get(request, *args, **kwargs)

############## Aluno #######################
class AlunoCreate(CreateView):
    model = Aluno #modelos usados
    fields = '__all__'#quais atributos(todos)
    #fields = ['nome','matricula','cpf','turma']
    #field__turma = Turma.objects.all().order_by('turma__nome')
    template_name = 'novo_aluno.html'#qual templete vai camar
    success_url = '/alunos/' #qual url vai redirecionar
    #fields = ['first_name', 'email']
    '''
    def post(self,request, *args, **kwargs):
        self.turma =  Turma.objects.get(pk=3)
        return super(AlunoCreate, self).post(request, *args, **kwargs)
    '''
    def get(self, request, *args, **kwargs):
        if not self.request.user.perfil.gerenciar_Alunos:
            return redirect('/sempermissao')
        return super(AlunoCreate, self).get(request, *args, **kwargs)

#List view (lista todos alunos)
def alunos(request):
    if not request.user.perfil.gerenciar_Alunos:
        return redirect('/sempermissao')
    #Entry.objects.order_by(Lower('headline').desc())
    alunos = Aluno.objects.all().order_by('nome')
    return render(request,'alunos.html',{'alunos':alunos})

def alunoDetalhes(request,pk):
    if not request.user.perfil.gerenciar_Alunos:
        return redirect('/sempermissao')
    aluno = Aluno.objects.get(pk=pk)
    autorizacaoAlunos = AutorizacaoAluno.objects.filter(aluno =aluno).order_by('-data')
    autorizacaoTurma = AutorizacaoTurma.objects.filter(turma = aluno.turma ).order_by('-data')
    return render(request,'alunoDetalhes.html',{'aluno':aluno,'autorizacaoAlunos':autorizacaoAlunos,'autorizacaoTurma':autorizacaoTurma})

class AlunoUpdate(UpdateView):
    model = Aluno
    fields = '__all__'#quais atributos(todos)
    #form_class = ProvaForm
    success_url = '/alunos/'
    template_name = 'update.html'

    def get(self, request, *args, **kwargs):
        if not self.request.user.perfil.gerenciar_Alunos:
            return redirect('/sempermissao')
        return super(AlunoUpdate, self).get(request, *args, **kwargs)


class AlunoDelete(DeleteView):
    model = Aluno
    success_url = '/alunos/'
    template_name = 'delete.html'

    def get(self, request, *args, **kwargs):
        if not self.request.user.perfil.gerenciar_Alunos:
            return redirect('/sempermissao')
        return super(AlunoDelete, self).get(request, *args, **kwargs)


############## Autorizacao Aluno #######################
class AutorizacaoAlunoCreate(CreateView):
    model = AutorizacaoAluno #modelos usados
    fields = '__all__'#quais atributos(todos)
    template_name = 'nova_autorizacao_aluno.html'#qual templete vai camar
    success_url = '/autorizacao_alunos/' #qual url vai redirecionar

    def get(self, request, *args, **kwargs):
        if not self.request.user.perfil.gerenciar_Autorizacao_Alunos:
            return redirect('/sempermissao')
        return super(AutorizacaoAlunoCreate, self).get(request, *args, **kwargs)

def autorizacaoAlunoCreateEspecifico(request,pk):
    if not request.user.perfil.gerenciar_Autorizacao_Alunos:
        return redirect('/sempermissao')
    erro = ''
    aluno = Aluno.objects.get(pk=pk)
    data_atual = datetime.now
    if  request.method == "POST":
        motivo = request.POST.get("motivo")
        #data = request.POST.get("data")
        observacoes = request.POST.get("observacoes")

        autorizacaoAluno = AutorizacaoAluno()
        try:
            autorizacaoAluno.motivo = motivo
            #autorizacaoAluno.data = data
            autorizacaoAluno.observacoes = observacoes
            autorizacaoAluno.aluno = aluno
            autorizacaoAluno.save()
            return redirect('/autorizacao_alunos')
        except Exception as e:
            erro = str(e)
            #return JsonResponse({"Erro":"Formulario invalido"},safe=True,status=400)
            return render(request,'nova_autorizacao_aluno_especifico.html',{'aluno':aluno, 'data_atual':data_atual,'erro':erro})

    return render(request,'nova_autorizacao_aluno_especifico.html',{'aluno':aluno, 'data_atual':data_atual,'erro':erro})



def autorizacaoAluno(request):
    if not request.user.perfil.gerenciar_Autorizacao_Alunos:
        return redirect('/sempermissao')
    autorizacaoAlunos = AutorizacaoAluno.objects.all().order_by('-data')
    return render(request,'autorizacaoAlunos.html',{'autorizacaoAlunos':autorizacaoAlunos})

def autorizacaoAlunoDetalhes(request,pk):
    if not request.user.perfil.gerenciar_Autorizacao_Alunos:
        return redirect('/sempermissao')
    autorizacaoAluno = AutorizacaoAluno.objects.get(pk=pk)
    return render(request,'autorizacaoAlunosDetalhes.html',{'autorizacaoAluno':autorizacaoAluno})

class AutorizacaoAlunoUpdate(UpdateView):
    model = AutorizacaoAluno
    fields = '__all__'#quais atributos(todos)
    #form_class = ProvaForm
    success_url = '/autorizacao_alunos/'
    template_name = 'update.html'

    def get(self, request, *args, **kwargs):
        if not self.request.user.perfil.gerenciar_Autorizacao_Alunos:
            return redirect('/sempermissao')
        return super(AutorizacaoAlunoUpdate, self).get(request, *args, **kwargs)

class AutorizacaoAlunoDelete(DeleteView):
    model = AutorizacaoAluno
    success_url = '/autorizacao_alunos/'
    template_name = 'delete.html'

    def get(self, request, *args, **kwargs):
        if not self.request.user.perfil.gerenciar_Autorizacao_Alunos:
            return redirect('/sempermissao')
        return super(AutorizacaoAlunoDelete, self).get(request, *args, **kwargs)


############## Autorizacao Turma #######################
class AutorizacaoTurmaCreate(CreateView):
    model = AutorizacaoTurma #modelos usados
    fields = '__all__'#quais atributos(todos)
    template_name = 'nova_autorizacao_turma.html'#qual templete vai camar
    success_url = '/autorizacao_turmas/' #qual url vai redirecionar

    def get(self, request, *args, **kwargs):
        if not self.request.user.perfil.gerenciar_Autorizacao_Turmas:
            return redirect('/sempermissao')
        return super(AutorizacaoTurmaCreate, self).get(request, *args, **kwargs)

def autorizacaoTurmaCreateEspecifica(request,pk):
    if not request.user.perfil.gerenciar_Autorizacao_Turmas:
        return redirect('/sempermissao')
    erro = ''
    turma = Turma.objects.get(pk=pk)
    data_atual = datetime.now
    if  request.method == "POST":
        motivo = request.POST.get("motivo")
        #data = request.POST.get("data")
        observacoes = request.POST.get("observacoes")

        autorizacaoTurma = AutorizacaoTurma()
        try:
            autorizacaoTurma.motivo = motivo
            #autorizacaoTurma.data = data
            autorizacaoTurma.observacoes = observacoes
            autorizacaoTurma.turma = turma
            autorizacaoTurma.save()
            return redirect('/autorizacao_turmas')
        except Exception as e:
            erro = str(e)
            #return JsonResponse({"Erro":"Formulario invalido"},safe=True,status=400)
            return render(request,'nova_autorizacao_turma_especifica.html',{'turma':turma, 'data_atual':data_atual,'erro':erro})

    return render(request,'nova_autorizacao_turma_especifica.html',{'turma':turma, 'data_atual':data_atual,'erro':erro})




def autorizacaoTurma(request):
    if not request.user.perfil.gerenciar_Autorizacao_Turmas:
        return redirect('/sempermissao')
    autorizacaoTurmas = AutorizacaoTurma.objects.all().order_by('-data')
    return render(request,'autorizacaoTurmas.html',{'autorizacaoTurmas':autorizacaoTurmas})

def autorizacaoTurmaDetalhes(request,pk):
    if not request.user.perfil.gerenciar_Autorizacao_Turmas:
        return redirect('/sempermissao')
    autorizacaoTurma = AutorizacaoTurma.objects.get(pk=pk)
    return render(request,'autorizacaoTurmasDetalhes.html',{'autorizacaoTurma':autorizacaoTurma})

class AutorizacaoTurmaUpdate(UpdateView):
    model = AutorizacaoTurma
    fields = '__all__'#quais atributos(todos)
    #form_class = ProvaForm
    success_url = '/autorizacao_turmas/'
    template_name = 'update.html'

    def get(self, request, *args, **kwargs):
        if not self.request.user.perfil.gerenciar_Autorizacao_Turmas:
            return redirect('/sempermissao')
        return super(AutorizacaoTurmaUpdate, self).get(request, *args, **kwargs)


class AutorizacaoTurmaDelete(DeleteView):
    model = AutorizacaoTurma
    success_url = '/autorizacao_turmas/'
    template_name = 'delete.html'

    def get(self, request, *args, **kwargs):
        if not self.request.user.perfil.gerenciar_Autorizacao_Turmas:
            return redirect('/sempermissao')
        return super(AutorizacaoTurmaDelete, self).get(request, *args, **kwargs)




'''
#List view (lista todos alunos)
def alunos(request):
    alunos = Aluno.objects.all()
    return render(request,'alunos.html',{'alunos':alunos})

def alunoDetalhes(request,pk):
    aluno = Aluno.objects.get(pk=pk)
    return render(request,'alunoDetalhes.html',{'aluno':aluno})

class AlunoUpdate(UpdateView):
    model = Aluno
    fields = '__all__'#quais atributos(todos)
    #form_class = ProvaForm
    success_url = '/alunos/'
    template_name = 'update.html'

class AlunoDelete(DeleteView):
    model = Aluno
    success_url = '/alunos/'
    template_name = 'delete.html'
'''
