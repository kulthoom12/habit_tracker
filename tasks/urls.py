from django.urls import path
from . import views

urlpatterns = [
  path( '', views.task_lis, name='task_list')
  path('task/create/',view.task_create, name='task_create'),
  path('task/update<int:pk>/', views.task_update, name='task_update'),
  path('task/delet/<int:pk>/', views.task_delete, name='task_delete'),
  path('task/clear_completed/', views.clear_complted, name='clear_completed'),

]