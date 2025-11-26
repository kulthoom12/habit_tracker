from django.urls import path
from . import views

urlpatterns = [
    path('', views.habit_list, name='habit_list'), 
    path('habit/create/', views.habit_create, name='habit_create'),
    path('habit/update/<int:pk>/', views.habit_update, name='habit_update'),
    path('habit/delete/<int:pk>/', views.habit_delete, name='habit_delete'),
    path('habit/clear_completed/', views.clear_completed, name='clear_completed'),
]
