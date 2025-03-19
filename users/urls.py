from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),  # Usando a view SignUpView baseada em classe
    path('login/', views.LoginView.as_view(), name='login'),  # URL de login (se for uma view baseada em classe)
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]
