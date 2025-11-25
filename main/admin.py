from django.contrib import admin
from .models import Task
# Register your models here.


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao', 'usuario', 'data_limite', 'criado_em')
    list_filter = ('concluida', 'prioridade')
    search_field=('titulo',)