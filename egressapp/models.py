from django.db import models
from datetime import date
from datetime import datetime
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Turma(models.Model):
    nome = models.CharField(max_length=20,unique=True)
    descricao = models.CharField(max_length=50)
    def __str__(self):
        return str(self.nome)
    #funcao que faz com que os campos sejam Maiusculo automaticamente
    def save(self, force_insert=False, force_update=False):
        self.nome = self.nome.upper()
        #self.descricao = self.descricao.upper()
        super(Turma, self).save(force_insert, force_update)

class Aluno(models.Model):
    nome = models.CharField(max_length=50)
    matricula = models.CharField(max_length=15,unique=True)
    cpf = models.CharField(max_length=11,unique=True)
    #Turma = models.ForeignKey(Turmas,on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.nome)
    #funcao que faz com que os campos sejam Maiusculo automaticamente
    def save(self, force_insert=False, force_update=False):
        self.nome = self.nome.upper()
        self.matricula = self.matricula.upper()
        super(Aluno, self).save(force_insert, force_update)

class AutorizacaoAluno(models.Model):
    motivo = models.CharField(max_length=100)
    #data = models.DateTime()
    data = models.DateTimeField(default=datetime.now)
    #data = models.DateField(null = True, blank = True)
    #Turma = models.ForeignKey(Turmas,on_delete=models.CASCADE)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    observacoes = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return "Autorização para: "+ str(self.aluno) +" Motivo: "+ str(self.motivo) +" Data: " +str(self.data)
    #funcao que faz com que os campos sejam Maiusculo automaticamente
    def save(self, force_insert=False, force_update=False):
        self.motivo = self.motivo.upper()
        super(AutorizacaoAluno, self).save(force_insert, force_update)

    #def __str__(self):
    #    return str(self.motivo)

class AutorizacaoTurma(models.Model):
    motivo = models.CharField(max_length=100)
    #data = models.DateTime()
    data = models.DateTimeField(default=datetime.now)
    #data = models.DateField(null = True, blank = True)
    #Turma = models.ForeignKey(Turmas,on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    observacoes = models.CharField(max_length=100, blank=True,null=True)

    def __str__(self):
        return "Autorização para: "+ str(self.turma) +" Motivo: '"+ str(self.motivo) +"' Data: " +str(self.data)
    #funcao que faz com que os campos sejam Maiusculo automaticamente
    def save(self, force_insert=False, force_update=False):
        self.motivo = self.motivo.upper()
        super(AutorizacaoTurma, self).save(force_insert, force_update)
    #def __str__(self):
    #    return str(self.motivo)


class Perfil(models.Model):
    #quando se usar OneToOneField
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gerenciar_Liberacao_Alunos = models.BooleanField(default = True)
    gerenciar_Alunos = models.BooleanField(default = False)
    gerenciar_Turmas = models.BooleanField(default = False)
    gerenciar_Autorizacao_Turmas = models.BooleanField(default = False)
    gerenciar_Autorizacao_Alunos = models.BooleanField(default = False)
    gerenciar_Relatorios = models.BooleanField(default = False)
    gerenciar_Usuarios = models.BooleanField(default = False)
    gerenciar_Permissoes_Usuarios = models.BooleanField(default = False)


    def __str__(self):
        return self.user.username

#usar isso para criar automaticamente um perfil
@receiver(post_save, sender=User)
def create_user_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)
#usar isso para criar automaticamente um perfil
@receiver(post_save, sender=User)
def save_user_perfil(sender, instance, **kwargs):
    instance.perfil.save()




'''
    idade = models.PositiveIntegerField(null = True)
    telefone1 = models.CharField(max_length=20)
    telefone2 = models.CharField(max_length=20)
    uf = models.CharField(max_length=2)
    cidade = models.CharField(max_length=30)
    endereco = models.CharField(max_length=300)
    tipo_usuario  = models.CharField(max_length=20)

    categoria = models.ForeignKey(Categoria)
    nome = models.CharField(max_length=100)
    #descricao = model.TextField()
    #foto = model.ImageField()
    def __str__(self):
        return str(self.nome)
'''

'''
    Resetar a senha do usuario

    >>python manage.py shell
    >>from django.contrib.auth.models import User
    >>User.objects.filter(is_superuser=True)

    >>usr = User.objects.get(username='nome_user')
    >>usr.set_password('nova_senha')
    >>usr.save()
'''
'''
    createsuperuser
'''
