from django.urls import path
from . import views

urlpatterns = [
    path('', views.habits_list, name='home'),
    path('habits/create/', views.habits_create, name='habits_create'),
    path('habits/update/<int:pk>/', views.habits_update, name='habits_update'),
    path('habits/delete/<int:pk>/', views.habits_delete, name='habits_delete'),
    path('habits/clear_completed/', views.clear_completed, name='habits_clear_completed'),

    path('login/', views.login_view, name='login'), 
    path('register/', views.register, name='register'),
]