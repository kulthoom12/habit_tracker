from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    path('', views.home, name='home'),

    path('habits/add/', views.habit_form, name='habits_create'),
    path('habits/edit/<int:pk>/', views.habit_form, name='habits_update'),
    path('habits/delete/<int:pk>/', views.habits_delete, name='habits_delete'),
    path('habits/clear_completed/', views.habits_clear_completed, name='habits_clear_completed'),
]