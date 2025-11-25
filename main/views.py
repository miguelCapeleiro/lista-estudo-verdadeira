from django.shortcuts import render
from .models import Task
# Create your views here.

def task_list(request):
    tarefas = Task.objects.all()
    context = {
        'tarefas':tarefas
    }

    return render(request, 'tasks/task_list.html', context)