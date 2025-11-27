from django.urls import path
from . import views

urlpatterns = [
    # Register and Login views
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    
    # Habit Views
    path('habits/', views.habits_list, name='habits_list'),
    path('habits/add/', views.habit_form, name='add_habit'),
    path('habits/edit/<int:pk>/', views.habit_form, name='edit_habit'),
    path('habits/delete/<int:pk>/', views.habits_delete, name='delete_habit'),
    path('habits/clear_completed/', views.habits_clear_completed, name='clear_completed_habits'),
]