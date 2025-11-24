from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='home'),
    path('task/create/', views.task_create, name='task_create'),
    path('task/update/<int:pk>/', views.task_update, name='task_update'),
    path('task/delete/<int:pk>/', views.task_delete, name='task_delete'),
    path('task/clear_completed/', views.clear_completed, name='clear_completed'),
]
