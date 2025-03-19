from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import UserSignupForm
from django.contrib.auth.views import LoginView

class SignUpView(CreateView):
    form_class = UserSignupForm  # Formulário para cadastro
    success_url = reverse_lazy('login')  # Redireciona para a página de login após o cadastro
    template_name = "users/signup.html"  # Template que será renderizado para o cadastro

class LoginView(LoginView):
    template_name = 'users/login.html'  # Template de login
    success_url = reverse_lazy('task_list')  # Redireciona para a lista de tarefas após o login