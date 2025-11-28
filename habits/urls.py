from django.urls import path
from . import views

urlpatterns = [
    # Register and Login views
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    
    # Habit Views
    path('', views.home, name='home'),
    path('habits/add/', views.habit_form, name='habits_create'),
    path('habits/edit/<int:pk>/', views.habit_form, name='habits_update'),
    path('habits/delete/<int:pk>/', views.habits_delete, name='habits_delete'),
    path('habits/clear_completed/', views.habits_clear_completed, name='habits_clear_completed'),
]