from django.db import models
from django.conf import settings
# Create your models here.
class Task(models.Model):

    class Priority(models.TextChoices):
        BAIXA = 'B', 'BAIXA'
        MEDIA = 'M', 'MEDIA'
        ALTA =  'A', 'ALTA'

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='tasks',
        null=True,
        blank=True

    )
    titulo = models.CharField('Titulo', max_length=100)
    descricao = models.TextField('Descrição', null=True,blank=True)
    concluida = models.BooleanField('Concluida', default= False)
    prioridade = models.CharField(
        'Prioridade',
        max_length=1, # Correct for single-letter codes
        choices=Priority.choices,
        default=Priority.MEDIA
    )
    
    data_limite = models.DateField('Data Limite', null=True, blank = True)
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado Em', auto_now=True)

    class Meta:
        ordering = ['concluida', 'data_limite', 'prioridade', 'criado_em']

        def __str__(self) -> str:
            return self.titulo