from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),  # Página inicial com a lista de tarefas
    path('task/new/', views.task_create, name='task_create'),  # Página para criar uma nova tarefa
    path('task/<int:pk>/edit/', views.task_update, name='task_update'),  # Página para editar uma tarefa existente
    path('task/<int:pk>/delete/', views.task_delete, name='task_delete'),  # Página para excluir uma tarefa
]
