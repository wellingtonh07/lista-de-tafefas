from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  # Usando o User padrão do Django

class UserSignupForm(UserCreationForm):
    # Adicionando campos customizados: nome e email
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'password1', 'password2')  # Utiliza os campos padrão de User + nome e email

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user
