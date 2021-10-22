from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='Sudoku'),
    path ('Start/', views.start, name='Start'),
    path('Generate/', views.GenerateButton, name='Generate'),
    path('Solve/', views.SolveButton, name='Solve'),
]