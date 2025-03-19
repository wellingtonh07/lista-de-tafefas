from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm

# Lista todas as tarefas
def task_list(request):
    tasks = Task.objects.all()  # Pega todas as tarefas do banco
    return render(request, 'lista/task_list.html', {'tasks': tasks})

# Cria uma nova tarefa
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)  # Preenche o formulário com os dados recebidos
        if form.is_valid():  # Verifica se os dados são válidos
            form.save()  # Salva a nova tarefa no banco
            return redirect('task_list')  # Redireciona para a lista de tarefas
    else:
        form = TaskForm()  # Exibe um formulário em branco para criação de tarefa
    return render(request, 'lista/task_form.html', {'form': form})

# Edita uma tarefa existente
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)  # Busca a tarefa pelo ID (pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)  # Preenche o formulário com os dados da tarefa
        if form.is_valid():
            form.save()  # Atualiza a tarefa
            return redirect('task_list')  # Redireciona para a lista de tarefas
    else:
        form = TaskForm(instance=task)  # Exibe o formulário preenchido com os dados da tarefa
    return render(request, 'lista/task_form.html', {'form': form})

# Exclui uma tarefa
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)  # Busca a tarefa pelo ID (pk)
    task.delete()  # Exclui a tarefa do banco de dados
    return redirect('task_list')  # Redireciona para a lista de tarefas
