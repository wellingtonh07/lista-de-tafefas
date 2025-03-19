# Lista de Tarefas - Django

Este é um projeto de **Lista de Tarefas** desenvolvido com **Django** e **Bootstrap**. O objetivo é fornecer uma plataforma simples para os usuários gerenciarem suas tarefas, com funcionalidades básicas como adicionar, editar e remover tarefas. O sistema permite que os usuários visualizem suas tarefas em uma lista e modifiquem seu conteúdo conforme necessário.

## Funcionalidades

- **Cadastro e Login**: O usuário deve estar logado para poder acessar a lista de tarefas. Caso não esteja autenticado, será solicitado que o usuário crie uma conta ou faça login.
- **Adicionar Tarefa**: Usuários autenticados podem adicionar novas tarefas à sua lista.
- **Editar Tarefa**: Usuários podem editar detalhes das tarefas existentes.
- **Excluir Tarefa**: Permite a exclusão de tarefas.
- **Priorização de Tarefas**: Cada tarefa pode ter uma prioridade (Alta, Média, Baixa), que é destacada com cores diferentes (vermelho, amarelo e verde).
- **Interface Responsiva**: O projeto utiliza o **Bootstrap** para garantir que a interface seja responsiva e funcional em dispositivos móveis e desktop.

## Tecnologias Utilizadas

- **Django**: Framework de desenvolvimento web em Python.
- **Bootstrap 5**: Framework front-end para design responsivo e elegante.
- **Python 3.x**: Linguagem de programação utilizada para o desenvolvimento do back-end.

## Como Rodar o Projeto

1. Clone este repositório para a sua máquina local:

   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   ```

2. Navegue até o diretório do projeto:

   ```bash
   cd nome-do-repositorio
   ```

3. Crie um ambiente virtual e ative-o:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Para MacOS/Linux
   venv\Scripts\activate     # Para Windows
   ```

4. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

5. Aplique as migrações do banco de dados:

   ```bash
   python manage.py migrate
   ```

6. Crie um superusuário para acessar a área administrativa (opcional):

   ```bash
   python manage.py createsuperuser
   ```

7. Execute o servidor de desenvolvimento:

   ```bash
   python manage.py runserver
   ```

8. Acesse o projeto em [http://127.0.0.1:8000](http://127.0.0.1:8000) no seu navegador.

## Contribuindo

1. Faça um fork deste repositório.
2. Crie uma branch para sua funcionalidade (`git checkout -b minha-nova-funcionalidade`).
3. Faça commit das suas alterações (`git commit -am 'Adiciona nova funcionalidade'`).
4. Envie para o repositório remoto (`git push origin minha-nova-funcionalidade`).
5. Abra um Pull Request.

