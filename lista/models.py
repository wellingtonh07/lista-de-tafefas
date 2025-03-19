from django.db import models

class Task(models.Model):
    # Opções para o campo de prioridade
    PRIORITY_CHOICES = [
        ('low', 'Baixa'),
        ('medium', 'Média'),
        ('high', 'Alta'),
    ]

    # Opções para o campo de status
    STATUS_CHOICES = [
        ('todo', 'A Fazer'),
        ('in_progress', 'Em Progresso'),
        ('done', 'Concluída'),
    ]

    # O título da tarefa
    title = models.CharField(max_length=200)
    
    # Descrição detalhada da tarefa (campo opcional)
    description = models.TextField(blank=True, null=True)
    
    # Data e hora de criação da tarefa, preenchida automaticamente
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Data limite para a conclusão da tarefa (campo opcional)
    due_date = models.DateTimeField(blank=True, null=True)
    
    # Status da tarefa (pode ser 'A Fazer', 'Em Progresso' ou 'Concluída')
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,  # Limita as opções para os valores definidos em STATUS_CHOICES
        default='todo'  # Valor padrão 'A Fazer'
    )
    
    # Prioridade da tarefa (pode ser 'Baixa', 'Média' ou 'Alta')
    priority = models.CharField(
        max_length=20,
        choices=PRIORITY_CHOICES,  # Limita as opções para os valores definidos em PRIORITY_CHOICES
        default='medium'  # Valor padrão 'Média'
    )

    # Método que retorna o título da tarefa para uma visualização mais legível
    def __str__(self):
        return self.title

    class Meta:
        # Ordena as tarefas para que as mais recentes apareçam primeiro
        ordering = ['-created_at']

# Comentários:
# 1. O modelo 'Task' é utilizado para representar uma tarefa dentro do sistema.
# 2. O campo 'title' é obrigatório e serve para identificar a tarefa.
# 3. A 'description' é opcional e pode ser usada para fornecer mais detalhes sobre a tarefa.
# 4. 'created_at' é preenchido automaticamente com a data e hora de criação da tarefa.
# 5. 'due_date' é a data limite para a tarefa ser concluída e é opcional.
# 6. 'status' permite acompanhar o progresso da tarefa, com valores predefinidos.
# 7. 'priority' define a prioridade da tarefa, sendo possível escolher entre 'Baixa', 'Média' ou 'Alta'.
# 8. O método '__str__' garante que, ao exibir a tarefa, o título será mostrado de forma legível.
# 9. A classe 'Meta' define a ordenação, garantindo que as tarefas mais recentes sejam exibidas primeiro.
